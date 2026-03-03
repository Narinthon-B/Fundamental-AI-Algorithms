# Searching algorithms

Searching algorithms เป็นรากฐานสำคัญของ Artificial Intelligence ที่ใช้ในการแก้ปัญหาหลากหลายประเภท ตั้งแต่การวางแผนเส้นทาง (pathfinding) ในเกมและหุ่นยนต์ การแก้ปริศนา (puzzle solving) เช่น 8-puzzle และ Rubik's cube ไปจนถึงการตัดสินใจใน game playing และการค้นหาคำตอบที่เหมาะสมที่สุดในปัญหาที่มีพื้นที่สถานะ (state space) ขนาดใหญ่ ในหลายๆ กรณี AI จำเป็นต้องสำรวจพื้นที่ของความเป็นไปได้ต่างๆ เพื่อหาวิธีแก้ปัญหาที่ดีที่สุด ซึ่ง searching algorithms ทำหน้าที่เป็นกลไกหลักในการสำรวจพื้นที่เหล่านี้อย่างเป็นระบบ

## Graph Searching Algorithms (BFS & DFS)

โปรเจกต์นี้เป็นการสาธิตวิธีการทำงานของอัลกอริทึมการค้นหาในกราฟ (Graph Traversal) พื้นฐาน 2 รูปแบบ คือ **Breadth-First Search (BFS)** และ **Depth-First Search (DFS)**


<img width="600" height="600" alt="graph-BFS-DFS" src="https://github.com/user-attachments/assets/b345ef0b-8635-454e-8f9a-797585aad178" />


## Breadth-First Search (BFS)

**Concept:** สำรวจกราฟโดยขยายการค้นหาออกในแนวกว้าง

BFS จะสำรวจ Node ลูกในระดับเดียวกันให้ครบก่อนที่จะขยับลงไปในระดับที่ลึกขึ้น ใช้โครงสร้างข้อมูลแบบ Queue (FIFO - First In First Out) ในการเก็บ nodes ที่รอการสำรวจ ทำให้ nodes ที่ถูกค้นพบก่อนจะถูกสำรวจก่อน

algorithm เริ่มต้นด้วยการนำ start node เข้า queue จากนั้นในแต่ละรอบจะดึง node ออกจาก queue ตรวจสอบว่าเป็น goal node หรือไม่ ถ้าไม่ใช่ก็จะนำ neighbors ทั้งหมดที่ยังไม่เคยเยี่ยมชมเข้า queue และทำซ้ำจนกว่าจะพบ goal หรือ queue ว่างเปล่า
    
เหมาะสำหรับการหาเส้นทางที่สั้นที่สุด (Shortest Path), goal อยู่ตื้น, มี memory เพียงพอ, หรือต้องการสํารวจทุกความเป็นไปได้ในระดับเดียวกัน
    

## Depth-First Search (DFS)

**Concept:** สำรวจกราฟโดยไปให้ลึกที่สุดเท่าที่จะทําได้

DFS จะสำรวจ Node ลูกลงไปเรื่อยๆ ตามกิ่งแขนงนั้นจนกว่าจะเจอทางตัน แล้วจึงย้อนกลับ (Backtrack) มาสำรวจกิ่งอื่น การทำงานของ DFS ใช้โครงสร้างข้อมูลแบบ Stack (LIFO - Last In First Out) nodes ที่ถูกค้นพบล่าสุดจะถูกสำรวจก่อน ทำให้ algorithm ไปลึกลงไปเรื่อยๆ จนกว่าจะต้องย้อนกลับ
    
เหมาะสำหรับ goal อยู่ไม่ลึก, มี memory จํากัด, ต้องการสำรวจโครงสร้างทั้งหมดของกราฟ, การหา Cycle ในกราฟ หรือการแก้ปัญหา Maze

## Example Output
**Breadth-First Search (BFS)** เมื่อกําหนดให้เริ่มต้นที่ node B โดยจะทําการสํารวจเพื่อนบ้านทั้งหมดของ B ก่อน ค่อยไปสํารวจเพื่อนบ้านของ A, C, D, X ที่ยังไม่เคยไป


![EX-BFS](https://github.com/user-attachments/assets/b10382e9-cd1e-4e39-9d45-76040b401f45)


**Depth-First Search (DFS)** เมื่อกําหนดให้เริ่มต้นที่ node B โดยจะพยายามไปหาเพื่อนบ้านให้ลําดับการเดินทางยาวที่สุดก่อน เมื่อถึงลึกจนสุดแล้ว ค่อยย้อนกลับมาเพื่อไปหาเพื่อนบ้านที่เหลือที่ยังไม่เคยไป

![EX-DFS](https://github.com/user-attachments/assets/a274dce1-d903-4920-89d4-9c6c428411a0)
