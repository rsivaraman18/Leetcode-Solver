''' 929 Email Address '''

def email(emails):
    req_email = set()
    for email in emails:
        email = email.split('@')     
        local = email[0]
        domain = email[1]

        # Dot check
        local1 = local.split('.')
        local2 =''.join(local1)

        # Plus Check
        if '+' in local2:
            index = local2.find('+')
            localname = local2[0:index]
        else:
            localname=local2
        
        Fin_email = localname +'@' + domain
        req_email.add(Fin_email)
        
    print(len(req_email))
        
    


email(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
email(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
