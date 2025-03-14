import random
from faker import Faker
from models import db, Task, Category
from app import app

fake = Faker()

def generate_fake_data(num_tasks=100):
    with app.app_context():
        categories = Category.query.all()
        if not categories:
            print("No categories found. Please add some categories first.")
            return
        
        for _ in range(num_tasks):
            task_name = fake.sentence(nb_words=4)
            status = random.choice(["pending", "completed"])
            category = random.choice(categories)
            new_task = Task(name=task_name, status=status, category_id=category.id)
            
            db.session.add(new_task)
        
        db.session.commit()
        print(f"{num_tasks} fake tasks generated successfully!")

if __name__ == "__main__":
    generate_fake_data()