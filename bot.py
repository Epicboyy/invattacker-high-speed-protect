from Linephu.linepy import *
from Linephu.akad.ttypes import *


client = LINE()
client.log("Auth Token : " + str(client.authToken))

oepoll = OEPoll(client)

MySelf = client.getProfile()
print("My MID : " + MySelf.mid)


def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        client.rejectGroupInvitation(op.param1)
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
      
def NOTIFIED_INVITE_INTO_ROOM(op):
    try:
        client.leaveRoom(op.param1)
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_ROOM\n\n")
        return
        
      
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.NOTIFIED_INVITE_INTO_ROOM: NOTIFIED_INVITE_INTO_ROOM
})


while True:
    oepoll.trace()
