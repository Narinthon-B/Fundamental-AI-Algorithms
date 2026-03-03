# Tower of Hanoi

## Problem Statement

เรามีเสา 3 ต้น (A, B, C) และแผ่นดิสก์ที่มีขนาดต่างกัน $n$ แผ่น เป้าหมายคือย้ายดิสก์ทั้งหมดจากเสา A (Source) ไปยังเสา C (Target) โดยมีเงื่อนไขดังนี้:

1.  ย้ายได้ทีละ 1 แผ่นต่อครั้ง
 
2.  แผ่นที่ใหญ่กว่า **ห้าม** วางทับแผ่นที่เล็กกว่า
 
3.  สามารถใช้เสา B เป็นที่เสาพักชั่วคราวได้ (Auxiliary)

อัลกอริทึมมาตรฐานที่ใช้แก้ปัญหา Tower of Hanoi คือ Recursive Algorithm (การเรียกซ้ำ) ซึ่งใช้หลักการ Divide and Conquer (แบ่งแยกและเอาชนะ) โดยลดขนาดของปัญหาใหญ่ให้กลายเป็นปัญหาย่อยที่เล็กลงเรื่อยๆ จนถึงจุดที่แก้ได้ง่ายที่สุด (Base Case) กระบวนการทำงานสามารถอธิบายได้เป็น 3 ขั้นตอนหลักคือ:

1. ย้ายจานจำนวน n-1 ใบจากเสาต้นทาง (Source) ไปพักไว้ที่เสาพัก (Auxiliary) โดยใช้เสาเป้าหมายเป็นตัวพักชั่วคราว

2. ย้ายจานใบที่ใหญ่ที่สุด (ใบที่ n) จากเสาต้นทางไปยังเสาเป้าหมาย (Destination)

3. ย้ายจานจำนวน n-1 ใบจากเสาพัก (Auxiliary) ตามไปวางทับที่เสาเป้าหมาย (Destination)

## Example Output
ไฟล์ [TOHGame.py](https://github.com/Narinthon-B/Fundamental-AI-Algorithms/blob/main/Tower-of-Hanoi/TOHGame.py "TOHGame.py") คือ การแสดงลําดับการย้ายของดิสก์ A, B, C

![TOHGame](https://github.com/user-attachments/assets/d8d6ab51-18f7-4d2e-b041-dace0fa197e3)


ไฟล์ [TOH-user-Input.py](https://github.com/Narinthon-B/Fundamental-AI-Algorithms/blob/main/Tower-of-Hanoi/TOH-user-Input.py "TOH-user-Input.py") user สามารถป้อนค่า N ซึ่งหมายถึงจํานวนดิสก์ได้ และแสดงผลออกมาเป็นจํานวนครั้งที่มีการเคลื่อนย้ายดิสก์

![TOH-user-Input](https://github.com/user-attachments/assets/fdfe47d5-5aef-4b3c-962e-7bde1ae6494b)
