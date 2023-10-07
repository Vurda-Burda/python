#связь между view и db

from view import *
from db import *

# действия со справочником
def main_rout():
    
    while True:
        ans = action_user()
        match ans:
            case 1:
                add_info(get_info())
            case 2:
                search_info(data_from_search())
            case 3:
                change_user_info()
            case 4:
                remove_user_info()
            case 5:
                all_user_info()
            case 6:
                break
    
main_rout()