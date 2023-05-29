def getSQLAlchemyURI():
    # URI depends on [engine]://[username]:[password]@[localhost]/[database]
    return 'postgresql://postgres:12345@localhost/scheduller_kb'