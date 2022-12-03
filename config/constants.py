class STAT:
    UNKNOWN = -1
    DISCONNECTED = 0
    BAD = 1
    OK = 2
    GOOD = 3
    GREAT = 4

class MESSAGE_TYPE:
    INFO = 0
    CAUTION = 100
    WARNING = 200
    ERROR = 300
    CRITICAL = 400
    
class LATENCY:
    DISCONNECTED = -1
    GREAT = 0.02
    GOOD = 0.05
    OK = 0.15
    BAD = 0.2
