import pymongo

def main():

	my_client = pymongo.MongoClient("mongodb://localhost:27017/")

	mydb = my_client['my_database']
	dblist = my_client.list_database_names()
	print(dblist)

if __name__ == '__main__':
	main()