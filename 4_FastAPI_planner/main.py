import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация FastAPI приложения
app = FastAPI()

# Модель данных для задачи
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


# Временное хранилище для задач
tasks = {}


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    logger.info('Отработал GET запрос на все задачи.')
    return list(tasks.values())

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    logger.info(f'Отработал GET запрос для задачи id = {task_id}.')
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    task_id = len(tasks) + 1
    tasks[task_id] = task
    logger.info(f'Отработал POST запрос для создания задачи id = {task_id}.')
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    logger.info(f'Отработал PUT запрос для задачи id = {task_id}.')
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    logger.info(f'Отработал DELETE запрос для задачи id = {task_id}.')
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"detail": "Task deleted"}

# для запуска используем:  uvicorn main:app --reload
