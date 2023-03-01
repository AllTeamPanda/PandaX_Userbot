from ... import udB

def get_approved():
    return udB.get_key("PMPERMIT") or []


def approve_user(chat_id):
    ok = get_approved()
    if chat_id in ok:
        return True
    ok.append(chat_id)
    return udB.set_key("PMPERMIT", ok)


def disapprove_user(chat_id):
    ok = get_approved()
    if chat_id in ok:
        ok.remove(chat_id)
        return udB.set_key("PMPERMIT", ok)


def is_approved(chat_id):
    return chat_id in get_approved()
