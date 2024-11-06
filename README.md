# Ứng dụng PBL4 Snort

## Tổng quan
Ứng dụng này được thiết kế để phân tích và hiển thị các cảnh báo Snort trong giao diện Tkinter GUI. Nó sử dụng các công cụ như Snort để giám sát mạng, thu thập các cảnh báo và hiển thị thông tin này trong một giao diện người dùng đơn giản nhưng mạnh mẽ. Dự án này được phát triển để hỗ trợ giám sát và quản lý mạng, đặc biệt hữu ích trong môi trường nghiên cứu và thử nghiệm.

## Cấu trúc
Dự án có cấu trúc thư mục như sau:

### **assets/**
Chứa các tài nguyên như `alert.csv.txt` và `local.rules` được sử dụng bởi ứng dụng để xử lý cảnh báo Snort, lưu trữ file để test trước khi dùng trong máy ảo.

### **config/**
Các tệp cấu hình cho việc thiết lập ứng dụng trên các môi trường khác nhau (Windows và Ubuntu).

- `__init__.py`: Khởi tạo module cấu hình.
- `settings.py`: Chứa các cài đặt chung cho ứng dụng.
- `ubuntu_config.py`: Cấu hình cho môi trường Ubuntu (Môi trường Máy ảo - Môi trường dự án).
- `windows_config.py`: Cấu hình cho môi trường Windows (Môi trường dev, testing, code, xử lý).

### **data/**
Các tệp liên quan đến việc xử lý và lưu trữ dữ liệu.

- `__init__.py`: Khởi tạo module dữ liệu.
- `data_processing.py`: Các hàm và logic để xử lý và phân tích dữ liệu từ cảnh báo.

### **gui/**
Chứa các thành phần giao diện người dùng (GUI) được xây dựng bằng Tkinter.

- `__init__.py`: Khởi tạo module giao diện.
- `panel1.py`: Bảng điều khiển để hiển thị dữ liệu cảnh báo.
- `panel2.py`: Bảng điều khiển để hiển thị dữ liệu liên quan đến các mối đe dọa.
- `panel3.py`: Bảng điều khiển để quản lý và điều khiển cài đặt mạng.

### **logic**
Các thành phần xử lý logic ứng dụng.

- `__init__.py`: Khởi tạo module logic.
- `alert_logic.py`: Logic xử lý cảnh báo từ Snort.
- `threat_logic.py`: Logic xử lý các mối đe dọa được phát hiện từ cảnh báo.

### **logs**
Thư mục chứa các tệp log được tạo ra bởi ứng dụng, bao gồm dữ liệu cảnh báo và log hệ thống.

- `alert_csv.txt`: Lưu trữ các cảnh báo từ Snort.

### **utils**
Các hàm tiện ích được sử dụng trong toàn bộ dự án.

- `__init__.py`: Khởi tạo module tiện ích.
- `alert_reader.py`: Chứa các hàm để đọc và xử lý cảnh báo.
- `file_modifier.py`: Chứa các hàm để sửa đổi các tệp tin.
- `plot.py`: Các hàm để tạo biểu đồ và hình ảnh dựa trên dữ liệu cảnh báo.

### **venv/**
Thư mục chứa môi trường ảo (virtual environment).

### **.gitignore**
Chỉ định các tệp và thư mục mà Git sẽ bỏ qua.

### **main.py**
Điểm vào chính của ứng dụng.

### **README.md**
Tài liệu mô tả về dự án.

### **requirements.txt**
Danh sách các thư viện Python cần thiết để chạy ứng dụng.

### **settings.txt**
Tệp cấu hình chứa thông tin như `sid:1000008`, được sử dụng trong quá trình xử lý cảnh báo và thiết lập ứng dụng.

## Cách chạy ứng dụng
1. Cài đặt các thư viện phụ thuộc bằng lệnh sau:
    ```bash
    pip install -r requirements.txt
    ```
2. Chạy ứng dụng bằng cách sử dụng lệnh sau:
    ```bash
    python main.py
    ```

## Ghi chú thêm
- Dự án sử dụng Tkinter để xây dựng giao diện người dùng.
- Các tệp cấu hình cho cả môi trường Windows và Ubuntu đã được cung cấp trong thư mục `config/`.
- Ứng dụng được thiết kế để đọc cảnh báo Snort, phân tích chúng và hiển thị kết quả trong một giao diện thân thiện với người dùng. Người dùng có thể dễ dàng xem và phân tích các mối đe dọa mạng thông qua các bảng điều khiển trực quan.

## Cảm ơn
Cảm ơn bạn đã sử dụng ứng dụng PBL4 Snort. Chúng tôi hy vọng nó sẽ giúp ích cho công việc của bạn trong việc giám sát và bảo mật mạng.
