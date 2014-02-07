##Data storage flow in redis
Jobs stored in set, jobs is just phone-numbers

`jobs:all = set(+79110400044,+79212134576, ....)`
`jobs:new = set()`

when worker take jobs it move from jobs:new to jobs:active

jobs:active = set(+79110400044,+79212134576, ....)

when worker execute some magic to get result, if any (found, notfound, error) of result got, job put to jobs:done

jobs:done = set(+79500449933,....)

And depend of result put to on of sets below

jobs:result:error = set(+79500449933,....)
jobs:result:notfound = set(+79500449933,....)
jobs:result:found = set(+79500449933,....)

Save result of job:

job:+79213346733 = "file"|<error report>|"N"

Next group need to monitoring workers

workers:run = set(localhost:8888,localhost:8990)
workers:error = set()
workers:jobs:<workerID> = set()

proxy:all = set(8.8.8.0:3345, ... )
proxy:error = list[]
proxy:alive = list[]

get_jobs(<count>):

