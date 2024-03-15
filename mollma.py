def pack_log(log, filename):
    """
    Pack a log file into a tarball.

    Args:
        log (str): The path to the log file.
        filename (str): The name of the tarball file.
    """

    with tarfile.open(filename, "w:gz") as tar:
        tar.add(log, arcname=os.path.basename(log))

