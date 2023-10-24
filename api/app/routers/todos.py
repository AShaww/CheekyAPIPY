from fastapi import APIRouter, Depends, HTTPException, Path

router = APIRouter(
    prefix="/todos",
    tags=["todo"]
)


@router.get('/')
async def get_todo() -> dict:
    return {'data': todos}


todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]


@router.post('/')
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        'data': 'A todo has been added !'
    }


@router.put('/{id}')
async def update_todo(todo_id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == todo:
            todo['Activity'] = body['Activity']
            return {
                'data': f"Todo with id {todo} has been updated"
            }

    return {
        'data': f"Todo with this id number {todo_id} was not found !"
    }


@router.delete('/{id}')
async def delete_todo(todo_id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"todo with id {todo_id} has been deleted"
            }

        return {
            'data': f"Todo with this id number {todo_id} was not found !"
        }
