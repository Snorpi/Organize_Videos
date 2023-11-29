import os
import csv
from moviepy.editor import VideoFileClip


def get_video_lengths(directory_path):
    video_files = [f for f in os.listdir(directory_path) if f.endswith('.mp4')]

    video_info_list = []

    for video_file in video_files:
        video_path = os.path.join(directory_path, video_file)

        try:
            clip = VideoFileClip(video_path)
            duration = clip.duration
            clip.close()

            video_info = {
                'file_name': video_file,
                'file_path': video_path,
                'duration': duration
            }

            video_info_list.append(video_info)
        except Exception as e:
            print(f"Error processing {video_file}: {str(e)}")

    return video_info_list


def write_to_csv(video_info_list, output_csv):
    with open(output_csv, 'w', newline='') as csv_file:
        fieldnames = ['file_name', 'file_path', 'duration']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for video_info in video_info_list:
            writer.writerow(video_info)


if __name__ == "__main__":
    # Change the directory path to follow the one to your video folder.
    directory_path = r"C:\\Path\\To\\Video\\Folder"
    # Change the output directory. it's easiest just to use your desktop.
    output_directory = r"C:\\Path\\To\\Output"
    # you can change the name of the output CSV if you want.
    output_csv = os.path.join(output_directory, "video_info12.csv")

    if os.path.exists(directory_path):
        video_info_list = get_video_lengths(directory_path)

        write_to_csv(video_info_list, output_csv)

        print(f"CSV file '{output_csv}' created successfully.")
    else:
        print("Directory not found.")
