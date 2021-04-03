import math
import argparse


def periods():
    args.periods = math.log((int(args.payment) / (int(args.payment) - float(args.interest) / (12 * 100) *
                                                  int(args.principal))), 1 + float(args.interest) / (12 * 100))
    year = str(int(args.periods / 12))
    months = str(math.ceil(args.periods % 12))
    overpayment = math.ceil(args.periods) * int(args.payment) - int(args.principal)
    if months == '12':
        year = str(int(year) + 1)
        months = '0'
    if year == '1':
        year += ' year'
    else:
        year += ' years'
    if months == '1':
        months += ' month'
    else:
        months += ' months'
    if year == '0 years':
        print('It will take ' + months + ' to repay this loan!')
    elif months == '0 months':
        print('It will take ' + year + ' to repay this loan!')
    else:
        print('It will take ' + year + ' and ' + months + ' to repay this loan!')
    print('Overpayment = ' + str(overpayment))


def annuity_pay():
    i = float(args.interest) / (12 * 100)
    args.payment = int(args.principal) * ((i * (1 + i) ** int(args.periods)) / ((1 + i) ** int(args.periods) - 1))
    overpayment = int(args.periods) * math.ceil(args.payment) - int(args.principal)
    print('Your annuity payment = ' + str(math.ceil(args.payment)) + '!')
    print('Overpayment = ' + str(overpayment))


def principal():
    i = float(args.interest) / (12 * 100)
    args.principal = int(args.payment) / ((i * (1 + i) ** int(args.periods)) / ((1 + i) ** int(args.periods) - 1))
    overpayment = int(args.periods) * int(args.payment) - int(args.principal)
    print('Your loan principal = ' + str(int(args.principal)) + '!')
    print('Overpayment = ' + str(math.ceil(overpayment)))


def diff_payment():
    global sum_pay
    i = float(args.interest) / (12 * 100)
    for j in range(int(args.periods)):
        args.payment = (int(args.principal) / int(args.periods) +
                        i * (int(args.principal) - (int(args.principal) * ((j + 1) - 1)) / int(args.periods)))
        sum_pay += math.ceil(args.payment)
        print('Month ' + str(j + 1) + ': payment is ' + str(math.ceil(args.payment)))
    overpayment = sum_pay - int(args.principal)
    print('\n' + 'Overpayment = ' + str(math.ceil(overpayment)))


def check_pozitiv(value):
    if value == float and float(value) < 0:
        print('Incorrect parameters')
        quit()
    elif value == int and int(value) < 0:
        print('Incorrect parameters')
        quit()
    else:
        return value


sum_pay = 0
parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment', type=check_pozitiv)
parser.add_argument('--principal', type=check_pozitiv)
parser.add_argument('--periods', type=check_pozitiv)
parser.add_argument('--interest', type=check_pozitiv)
args = parser.parse_args()

if args.type and args.interest:
    if args.type == 'annuity':
        if not args.principal:
            principal()
        elif not args.payment:
            annuity_pay()
        elif not args.periods:
            periods()
    elif args.type == 'diff' and not args.payment:
        diff_payment()
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
