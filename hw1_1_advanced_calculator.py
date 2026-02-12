def calculate_statistics(numbers=list):
    d = {
    'mean':sum(numbers)/len(numbers),
    'med': numbers[(len(numbers)//2)] if len(numbers)%2==1 else (numbers[(len(numbers)//2)]+numbers[(len(numbers)//2)-1])/2,
    'min': min(numbers),
    'max': max(numbers),
    'sum': sum(numbers),
    }
    return d
print('калькулятор:\n', calculate_statistics([1,2,3,4,5,6]))

def process_string(text=str):
    d = {
    'word_count': len(text.split()),
    'sntc_count': len(text.split('.' and '!' and '?')),
    'reverse_str': ' '.join([text.split()[i] for i in range (len(text.split())-1, -1, -1)]),
    'letter_freq': [''.join([str(i),' : ',str((text.lower()).count(i))]) for i in set(sorted([_ for _ in text.lower() if _.isalpha()==True]))],
    }
    return d
print('строки:\n', process_string("Привет, мир! Как дела?"))

def validate_password(password=str):
    c=[i for i in password]+[int(i) for i in [i for i in password] if i in "0123456789"]
    errs=[]
    errs.append('короткий пароль!') if len(password)<8 else 0
    errs.append('нет цифр!') if not(any([type(i)==int for i in c])) else 0
    errs.append('нет заглавных букв!') if password.lower()==password else 0
    errs.append('нет строчных букв!') if password.upper()==password else 0
    errs.append('нет спец символов!') if len([i for i in c if str(i) in "!@#$%^&*"])==0 else 0
    a = True if len(errs)==0 else [False, errs]
    return a
print(validate_password('AHZ516'))