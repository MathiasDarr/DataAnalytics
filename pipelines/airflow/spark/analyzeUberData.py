def analyzeUberData(sc):
    ut = sc.textFile("/home/mddarr/DalinarSoftware/Pipelines/data/uber.csv")
    rows = ut.map(lambda line: line.split(","))
    count = rows.map(lambda row: row[0]).distinct().count()
    print(count)
    hockeyTeams = sc.parallelize(("wild", "blackhawks", "red wings", "wild", "oilers", "whalers", "jets", "wild"))
    hockeyTeams.map(lambda k: (k, 1)).countByKey().items()
    # hockeyTeams.saveAsTextFile("hockey_teams.txt")