# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",filemode="w",
#                     format="We have next logging message: "
#                            "%(asctime)s:%(levelname)s-%(message)s")
# try:
#     print(10/0)
# except Exception:
#     logging.debug("debug")
#     logging.info("info")
#     logging.warning("warning")
#     logging.error("error")
#     logging.critical("critical")
"""
>>> 2+2
5
"""
if __name__ == "__main":
    import doctest
    doctest.testmod()