import pygal

pie = pygal.Pie()
pie.title = "What is your favorite fruit?"
pie.add("Apple", 55)
pie.add("Strawberry", 20)
pie.add("Banana", 25)

pie.render_in_browser()