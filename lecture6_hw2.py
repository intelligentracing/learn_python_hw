# This file is for the Y2K homework question, and this is the solution:


# The storage of time began at Epoch at 1970, with a 4 byte 32 bit storage, which is a really big integer
# in seconds. In the year 2038, the time storage will be exceeded, meaning the sign bit will turn negative
# and there will be a runtime error(since time can't be negative). To avoid this we can use a 64 bit system,
# which guarantees us billions of more years, which means we don't have to worry about this time storage
# scenario again.