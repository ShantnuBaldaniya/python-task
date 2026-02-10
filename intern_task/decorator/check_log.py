user = {
    'a':'admin',
    'b':'user'
}

def check(func):
    def use(name):
        if name in user and user[name]=='admin':
            print('access grant! for :',name)
            func(name)
        else:
            print('access not grant! for :',name)
    return use
@check
def test(name):
    print('i m login for testing')

test('b')
test('shantnu')

