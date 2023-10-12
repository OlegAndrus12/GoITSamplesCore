from constants import SECONDS_IN_MINUTE

# annotations
def minutes_to_seconds(minutes: int) -> str: 
    print(type(minutes))
    res: int = minutes * SECONDS_IN_MINUTE
    return f"time is: {res}"

def minutes_to_milliseconds(minutes: int) -> str: 
    print(type(minutes))
    res: int = minutes * SECONDS_IN_MINUTE * 1000
    return f"time is: {res}"



if __name__ == "__main__":
    print(minutes_to_seconds(23))
    print(minutes_to_milliseconds(23))