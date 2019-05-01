files = {
    "ratings": "user_id,movie_id,rating,ts",
}
DELIM = ","
for name in files:
  with open("%s.dat" % name) as src:
    with open("%s.csv" % name, "w") as dst:
      headers = files[name] + "\n"
      data = src.read().replace(DELIM,"`").replace("::",DELIM)
      dst.write(headers + data)