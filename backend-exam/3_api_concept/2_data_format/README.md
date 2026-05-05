## Question
![](/assets/q_data_format.png)
## Response Section
JSON คือ text-based สามารถอ่านง่าย (human-readable) ส่วน Protocol Buffers (Protobuf) คือ binary format ที่ต้องมี schema (.proto) 

Ex. JSON
{
  "name": "John",
  "age": 30
}

Ex. .proto
syntax = "proto3";

message User {
  string name = 1;
  int32 age = 2;
}

JSON
    ข้อดี
        - ใช้ง่าย
        - debug ง่าย
        - ใช้กับ REST ได้ดี
    ข้อเสีย
        - size ใหญ่
        - parse ช้า

Protobuf
    ข้อดี
        - เร็วมาก
        - size เล็ก
        - เหมาะกับ microservices / gRPC
    ข้อเสีย
        - ต้อง compile
        - debug ยาก
        - อ่านไม่ได้ตรง ๆ