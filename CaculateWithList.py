class CaculateWithList():

    def list_a_and_b(a,b):
        r = list(set(a) & set(b))
        r.sort()
        return r

    def list_a_or_b(a,b):
        r = list(set(a) | set(b))
        r.sort()
        return r

    def list_a_have_b(a,b):
        r = list(set(a) - set(b))
        r.sort()
        return r
    def list_b_have_a(a,b):
        r = list(set(b) - set(a))
        r.sort()
        return r
    def list_not_have_a_and_b(a,b):
        r = list(set(a) ^ set(b))
        r.sort()
        return r