def getSQLAlchemyURI():
    # URI depends on [engine]://[username]:[password]@[localhost]/[database]
    return 'postgresql://postgres:admin#21@localhost/scheduller_kb'