import json

while True:
    U1 = input('<<Message 1>>: ')
    U2 = input('<<Message 2>>: ')
    
    conversation = {
    'Message_1': U1,
    'Message_2': U2
    }
    with open('Conversations.jsonl', 'a') as out:
        json.dump(conversation, out, indent=4)
        out.write('\n')

    C = input('Do you want to continue YES/NO: ')

    if C == 'NO':
        break