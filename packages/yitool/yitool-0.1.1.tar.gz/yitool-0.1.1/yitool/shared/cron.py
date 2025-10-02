from typing import List
from croniter import croniter
from enum import Enum
from datetime import datetime

class REPEAT_TYPE(Enum):
    MINUTE = 'minute'
    HOUR = 'hour'
    DAY = 'day'
    MONTH = 'month'
    WEEK = 'week'
    YEAR = 'year'
    
    @classmethod
    def get_repeat_type_by_value(cls, value: str) -> 'REPEAT_TYPE':
        for repeat_type in cls:
            if repeat_type.value == value:
                return repeat_type
        return None
    

class Cron(object):
    _base_time: datetime
    _repeat_type: REPEAT_TYPE
    
    def __init__(self, base_time: datetime, repeat_type: REPEAT_TYPE):
        self._base_time = base_time
        self._repeat_type = repeat_type
        self._iter = None
        
    @property
    def crontab_idxs(self) -> List[int]:
        idx_map = {
            REPEAT_TYPE.MINUTE: [0, 1, 2, 3, 4],
            REPEAT_TYPE.HOUR: [1, 2, 3, 4],
            REPEAT_TYPE.DAY: [2, 3, 4],
            REPEAT_TYPE.WEEK: [2, 3],
            REPEAT_TYPE.MONTH: [3, 4],
            REPEAT_TYPE.YEAR: [4],
        }
        return idx_map.get(self._repeat_type, -1)
        
    @property
    def base_time(self) -> datetime:
        return self._base_time
        
    @property
    def crontab(self) -> str:            
        year = self.base_time.year
        month = self.base_time.month
        day = self.base_time.day
        weekday = self.base_time.weekday()
        hour = self.base_time.hour
        minute = self.base_time.minute
        arr = [str(int_val) for int_val in [minute, hour, day, month, weekday]]
        for idx in self.crontab_idxs:
            arr[idx] = '*'
        return ' '.join(arr)
    
    def get_next(self, dt: datetime = None) -> datetime:
        if dt is not None and isinstance(dt, datetime):
            self._base_time = dt
        if self._iter is None:
            self._iter = croniter(self.crontab, self.base_time)
        return self._iter.get_next(datetime)
    

if __name__ == '__main__':
    for repeat_type in REPEAT_TYPE:
        cron = Cron(datetime.now(), repeat_type=repeat_type)
        print(repeat_type, cron.crontab)
        for _ in range(5):
            print(repeat_type, cron.get_next())