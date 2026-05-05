## Question
![](/assets/q_acid.png)
## Response Section
ACID คือชุดคุณสมบัติ 4 ข้อที่ทำให้ การทำงานของฐานข้อมูลแบบ transaction เชื่อถือได้ ประกอบด้วย
    - A : Atomicity คือ ข้อมูลจะต้องรันได้ทั้งหมด(Commit) หรือ รันไม่ได้ทั้งหมด(RollBack)
    - C : Consistency คือ ข้อมูลต้องครบถ้วนห้ามผิดเพี้ยน
    - I : Isolation คือ การรัน Database หลายตัวพร้อมกัน ข้อมูลต้องไม่ผิดเพี้ยน
    - D : Durability คือ ข้อมูลใน Database ต้องอยู่ครบถ้วน

ACID ในบทบาทของ Database ทำหน้าที่ดูความถูกต้องของข้อมูล
     ในบทบาทของ Application ทำหน้าที่เป็น Business Logic และ System Behavior