This Directory Contains The Code Files Created By Jaivin Jacob


1. Datadownloader.ipynb - To  Downloads videos from URLs in a dataframe and creates a new CSV file, skipping videos with encoding errors. (default: "videos_1000")

2. VIT_GPT2.ipynb - Implementation of VIT model on the sample of original dataset

3. Feature_Extraction_Resnet50.ipynb - Extracting features from videos using pretrained Resnet50 model. Mapping between video ID and features.

4. Feature_Extraction_VIT.ipynb - Extracting features from videos using pretrained VIT model.

5. Custom_Model_Resnet_Features.ipynb - Created an LSTM model for generating text descriptions from features extracted using Resnet50 model.

6. VIT_GPT2_Full_Pipeline.ipynb - Full code which: 1. generating text description using VIT gpt, 2. Converting to audio file, 3. Finding silent part in the video(handles videos with background music), 4. Merge audio description with the video.

7. SpaceTimeGPT_FineTunining.ipynb - Code to process the data for SpaceTime GPT, finetune the model and to generate text description with the pretrained model.

8. Blip_Bulk_Descriptions.ipynb - Full code to run BLIP model to generate captions.
