from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.users
users_collection = database.get_collection("users_entity")

# helpers
def user_helper(user) -> dict:
    return {
        "id" : str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "password":user["password"]
    }


# create a new user
async def create_user(user_data: dict) -> dict:
    user = await users_collection.insert_one(user_data)
    new_user = await users_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve all users present in the database
async def get_all_users():
    users = []
    async for user in users_collection.find():
        users.append(user_helper(user))
    return users

# get a user with matching ID
async def get_one_user(id: str):
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

# update a user with matching ID
async def update_user(id: str, data: dict):
    if len(data)<1:
        return False
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False 

#delete a user
async def delete_user(id: str):
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        await users_collection.delete_one({"_id": ObjectId(id)})
        return True
