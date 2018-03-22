import read
import dateutil

df = read.load_data()

df['parse_time'] = df['submission_time'].apply(lambda x : dateutil.parser.parse(x))

df['hour'] = df['parse_time'].apply(lambda x : x.hour)

print(df.hour.value_counts())
