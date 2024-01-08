from fastapi import HTTPException, Path, Body, APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from server.database import (
    create_user,
    update_user,
    delete_user,
    get_all_users,
    get_one_user
    
)
from server.models.user import (
    ResponseModel,
    ErrorResponseModel,
    UserCreateModel,
    UpdateUserModel
)

router = APIRouter()

#create user
@router.post("/create", response_description="User data added into the database")
async def create_user_data(user: UserCreateModel = Body(...)):
    user = jsonable_encoder(user)
    new_user = await create_user(user)
    return ResponseModel(new_user, "User added successfully!")

#get all users
@router.get("/all", response_description="Users retrieved")
async def get_all_users_data():
    users = await get_all_users()
    if users:
        return ResponseModel(users, "All Users data retrieved successfully")
    return ErrorResponseModel(users, "No users found 😟")

#get a user
@router.get("/{id}", response_description="User found")
async def get_user_data(id):
    user = await get_one_user(id)
    if user:
        return ResponseModel(user, "All Users data retrieved successfully")
    return ErrorResponseModel(user, "No users found 😟")

# update a user info
@router.put("/update/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in dict(req).items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "user name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

# delete user info
@router.delete("/delete/{id}", response_description="Student data deleted from the database")
async def delete_user_data(id: str):
    deleted_student = await delete_user(id)
    if deleted_student:
        return ResponseModel(
            "User with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(id)
    )
    