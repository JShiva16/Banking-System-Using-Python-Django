from django.utils import timezone
from django.db.models import Q

from celery.decorators import task

from accounts.models import UserBankAccount
from transactions.constants import INTEREST
from transactions.models import Transaction


@task(name="calculate_interest")
def calculate_interest():
    today = timezone.now().date()

    # Include accounts where interest has started (interest_start_date <= today)
    # or where interest_start_date is not set (we'll fall back to initial_deposit_date).
    accounts = UserBankAccount.objects.filter(
        balance__gt=0,
        initial_deposit_date__isnull=False,
    ).filter(
        Q(interest_start_date__lte=today) | Q(interest_start_date__isnull=True)
    ).select_related('account_type')

    this_month = timezone.now().month

    created_transactions = []
    updated_accounts = []

    for account in accounts:
        if this_month in account.get_interest_calculation_months():
            interest = account.account_type.calculate_interest(
                account.balance
            )
            account.balance += interest
            account.save()

            transaction_obj = Transaction(
                account=account,
                transaction_type=INTEREST,
                amount=interest
            )
            created_transactions.append(transaction_obj)
            updated_accounts.append(account)

    if created_transactions:
        Transaction.objects.bulk_create(created_transactions)

    if updated_accounts:
        UserBankAccount.objects.bulk_update(
            updated_accounts, ['balance']
        )
