# DEBUG_VERBOSE = 1
# DEBUG_VERBOSE = -2
# DEBUG_VERBOSE = -10
# DEBUG_VERBOSE = -11
DEBUG_VERBOSE = -11

# PROFILING_TYPE = "cProfile"
# PROFILING_TYPE = "vmprof"
# PROFILING_TYPE = None
PROFILING_TYPE = None

# PROFILING_OUTPUT_STYLE = "FILE"
# PROFILING_OUTPUT_STYLE = "TEXT"
PROFILING_OUTPUT_STYLE = "FILE"

# ENABLE_CYTHON_PROFILE = False
# ENABLE_CYTHON_PROFILE = True
ENABLE_CYTHON_PROFILE = False


HIT_UNEXPECTED_ERROR = False
HIT_UNEXPECTED_ERROR_MESSAGE = None

class NormalException(Exception):
  """Exception that is understood (not fatal/unexpected error) and handled elegantly"""
  pass

class UnderstoodException(Exception):
  """Exception that is understood (not fatal/unexpected error), but not handled elegantly"""
  pass