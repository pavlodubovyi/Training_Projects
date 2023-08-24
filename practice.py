import pickle
from time import sleep
from datetime import datetime

class RememberAll:
    def __init__(self, *args) -> None:
        self.data = list(args)
        self.saved = None
        self.restored = None
    
    def __getstate__(self) -> object:
        state = self.__dict__.copy() # якщо __dict__ в __getstate__, він бере всі методи з init
        state['saved'] = datetime.now()
        return state

if __name__ == "__main__":
    print(RememberAll.__dict__)
    r = RememberAll(1, 2, 3, 4, 5)
    print(r.data)
    r_dump = pickle.dumps(r)
    sleep(2)
    r_load = pickle.loads(r_dump)
    print(r.saved, r.restored)
    print(r_load.saved, r_load.restored)