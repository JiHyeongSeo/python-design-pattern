class HTTPConnection:
    def connect(self):
        print("http connect")


class FTPConnection:
    def connect(self):
        print("ftp connect")


class SimpleFactory(object):
    @staticmethod
    def build_connection(protocol):
        if protocol == "http":
            return HTTPConnection()
        elif protocol == "ftp":
            return FTPConnection()
        else:
            raise RuntimeError("Unknown protocol")


if __name__ == "__main__":
    PROTOCOL = "http"
    protocol = SimpleFactory.build_connection(PROTOCOL)
    protocol.connect()
