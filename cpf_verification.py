# A code that I made based in a Udemy course some time ago.
### CPF = Cadastro de Pessoa Física / Physical Person Register in english, like the Social Security Number (SSN)

def main():
    print("\033[92m====== CPF VALIDATOR ======\033[0m")
    cpf = input("\033[33mPlease, inform your CPF: \033[0m")
    cpf = verify_cpf(cpf)
    counter = 10
    new_cpf = cpf[:9]
    new_cpf = validate_cpf(new_cpf, counter)
    new_cpf = validate_cpf(new_cpf, counter+1)
    if new_cpf == cpf:
        print(
            f"\033[32mYour CPF {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:12]} is valid.\033[0m"
        )
    else:
        print(
            f"\033[31m{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:12]} is a invalid CPF.\033[0m"
        )


def validate_cpf(cpf, counter):
    total = 0
    for x in cpf:
        total += int(x)*counter
        counter -= 1
    total = (total * 10) % 11
    if total > 9:
        total = 0
    return str(cpf+str(total))


def verify_cpf(cpf):
    '''
    Verify the CPF length and remove dots or en dashes if necessary.
    '''
    if str(cpf).count('.') > 0:
        cpf = str(cpf).replace('.', '')
    if str(cpf).count('-') > 0:
        cpf = str(cpf).replace('-', '')

    if len(cpf) != 11:
        print("\033[31mInvalid CPF. A CPF must have 11 numbers.\033[0m\n")
        main()

    return (cpf)


main()
