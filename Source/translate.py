import pandas as pd
import numpy as np
path = "/mnt/c/Users/Quang Khai/Downloads/Nhom5/Dataset/country_comparison_large_dataset.csv"
df = pd.read_csv(path)
column_mapping = {
    'Country': 'Quốc gia',
    'Year': 'Năm',
    'GDP (in Trillions USD)': 'GDP (nghìn tỷ USD)',
    'GDP per Capita (in USD)': 'GDP bình quân đầu người (USD)',
    'Inflation Rate (%)': 'Tỷ lệ lạm phát (%)',
    'Population (in Millions)': 'Dân số (triệu người)',
    'Population Growth Rate (%)': 'Tỷ lệ tăng trưởng dân số (%)',
    'Urban Population (%)': 'Dân số đô thị (%)',
    'Life Expectancy (Years)': 'Tuổi thọ (năm)',
    'Healthcare Expenditure per Capita (USD)': 'Chi tiêu y tế bình quân đầu người (USD)',
    'Doctor-to-Patient Ratio': 'Tỷ lệ bác sĩ-bệnh nhân',
    'Literacy Rate (%)': 'Tỷ lệ biết chữ (%)',
    'Education Expenditure as % of GDP': 'Chi tiêu giáo dục (% GDP)',
    'Internet Penetration (%)': 'Tỷ lệ sử dụng Internet (%)',
    'Smartphone Adoption (%)': 'Tỷ lệ sử dụng điện thoại thông minh (%)',
    'Energy Consumption (TWh)': 'Tiêu thụ năng lượng (TWh)',
    'Renewable Energy Share (%)': 'Tỷ lệ năng lượng tái tạo (%)',
    'Military Expenditure (in Billion USD)': 'Chi tiêu quân sự (tỷ USD)',
    'Number of Active Military Personnel': 'Số lượng quân nhân tại ngũ',
    'CO2 Emissions (Million Metric Tons)': 'Lượng phát thải CO2 (triệu tấn)',
    'Forest Coverage (%)': 'Diện tích rừng che phủ (%)',
    'Number of Airports': 'Số lượng sân bay',
    'Road Network Length (in km)': 'Chiều dài mạng lưới đường bộ (km)',
    'Public Transport Usage (%)': 'Sử dụng phương tiện công cộng (%)',
    'Human Development Index (HDI)': 'Chỉ số phát triển con người (HDI)',
    'Gender Equality Index': 'Chỉ số bình đẳng giới',
    'Poverty Rate (%)': 'Tỷ lệ nghèo (%)',
    'Number of International Visitors (in Millions)': 'Số lượng khách quốc tế (triệu người)',
    'Tourism Revenue (in Billion USD)': 'Doanh thu du lịch (tỷ USD)',
    'Agricultural Land (%)': 'Diện tích đất nông nghiệp (%)',
    'Unemployment Rate (%)': 'Tỷ lệ thất nghiệp (%)',
    'Labor Force Participation Rate (%)': 'Tỷ lệ tham gia lực lượng lao động (%)',
    'Crime Rate (per 100,000)': 'Tỷ lệ tội phạm (trên 100,000 người)',
    'Corruption Perception Index': 'Chỉ số cảm nhận tham nhũng',
    'Freedom of Press Index': 'Chỉ số tự do báo chí',
    'Voting Participation Rate (%)': 'Tỷ lệ tham gia bầu cử (%)'
}

# Rename the columns
df.rename(columns=column_mapping, inplace=True)

print(df['Quốc gia'].unique())

# Dictionary mapping English country names to Vietnamese
country_translation = {
    'USA': 'Hoa Kỳ',
    'Russia': 'Nga',
    'Canada': 'Canada',
    'China': 'Trung Quốc',
    'India': 'Ấn Độ',
    'Australia': 'Úc'
}


#Translate the country names
df['Quốc gia'] = df['Quốc gia'].replace(country_translation)

# print(df['Quốc gia'].unique())

df.to_csv('/mnt/c/Users/Quang Khai/Downloads/Nhom5/Dataset/country_comparison_large_dataset_vn.csv', index=False, encoding='utf-8-sig')


































