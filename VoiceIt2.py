
import requests


class VoiceIt2:
    base_URL = 'https://api.voiceit.io'
    voiceit_basic_auth_credentials = ''

    def __init__(self, key, token):
        self.voiceit_basic_auth_credentials = (key, token)
        self.headers = {'platformId': '28'}

    def get_all_users(self):
        try:
            response = requests.get(self.base_URL + '/users', auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_phrases(self, lang):
        try:
            response = requests.get(self.base_URL + '/phrases/' + str(lang), auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_user(self):
        try:
            response = requests.post(self.base_URL + '/users', auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def check_user_exists(self, user_id):
        try:
            response = requests.get(self.base_URL + '/users/' + str(user_id), auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def delete_user(self, user_id):
        try:
            response = requests.delete(self.base_URL + '/users/' + str(user_id), auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_groups_for_user(self, user_id):
        try:
            response = requests.get(self.base_URL + '/users/' + str(user_id) + '/groups', auth=self.voiceit_basic_auth_credentials,
                                    headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_groups(self):
        try:
            response = requests.get(self.base_URL + '/groups', auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_group(self, group_id):
        try:
            response = requests.get(self.base_URL + '/groups/' + str(group_id), auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def group_exists(self, group_id):
        try:
            response = requests.get(self.base_URL + '/groups/' + str(group_id) + '/exists', auth=self.voiceit_basic_auth_credentials,
                                    headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_group(self, group_desc):
        dataObj = {}
        dataObj['description'] = group_desc
        try:
            response = requests.post(self.base_URL + '/groups', auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def add_user_to_group(self, group_id, user_id):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['userId'] = user_id
        try:
            response = requests.put(self.base_URL + '/groups/addUser', auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def remove_user_from_group(self, group_id, user_id):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['userId'] = user_id
        try:
            response = requests.put(self.base_URL + '/groups/removeUser', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                    headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def delete_group(self, group_id):
        try:
            response = requests.delete(self.base_URL + '/groups/' + str(group_id), auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_face_enrollments(self, user_id):
        try:
            response = requests.get(self.base_URL + '/enrollments/face/' + str(user_id), auth=self.voiceit_basic_auth_credentials,
                                    headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_voice_enrollments(self, user_id):
        try:
            response = requests.get(self.base_URL + '/enrollments/voice/' + str(user_id), auth=self.voiceit_basic_auth_credentials,
                                    headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_video_enrollments(self, user_id):
        try:
            response = requests.get(self.base_URL + '/enrollments/video/' + str(user_id), auth=self.voiceit_basic_auth_credentials,
                                    headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_voice_enrollment(self, user_id, lang, phrase, file_path):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        f = open(file_path, 'rb')
        filesObj = [('recording', ('enrollment.wav', f, 'audio/wav'))]
        try:
            response = requests.post(self.base_URL + '/enrollments/voice', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except  requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def create_voice_enrollment_by_url(self, user_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/enrollments/voice/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_face_enrollment(self, user_id, file_path, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['doBlinkDetection'] = blink_detection
        f = open(file_path, 'rb')
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/enrollments/face', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except  requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def create_face_enrollment_by_url(self, user_id, file_Url, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['doBlinkDetection'] = blink_detection
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/enrollments/face/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_video_enrollment(self, user_id, lang, phrase, file_path, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['doBlinkDetection'] = blink_detection
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        f = open(file_path, 'rb')
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/enrollments/video', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def create_video_enrollment_by_url(self, user_id, lang, phrase, file_Url, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['doBlinkDetection'] = blink_detection
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/enrollments/video/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_all_enrollments(self, user_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/' + str(user_id) + '/all', auth=self.voiceit_basic_auth_credentials,
                                       headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_all_face_enrollments(self, user_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/' + str(user_id) + '/face', auth=self.voiceit_basic_auth_credentials,
                                       headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_all_voice_enrollments(self, user_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/' + str(user_id) + '/voice', auth=self.voiceit_basic_auth_credentials,
                                       headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_all_video_enrollments(self, user_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/' + str(user_id) + '/video', auth=self.voiceit_basic_auth_credentials,
                                       headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_face_enrollment(self, user_id, face_enrollment_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/face/' + str(user_id) + '/' + str(face_enrollment_id),
                                       auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_voice_enrollment(self, user_id, voice_enrollment_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/voice/' + str(user_id) + '/' + str(voice_enrollment_id),
                                       auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_video_enrollment(self, user_id, video_enrollment_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/video/' + str(user_id) + '/' + str(video_enrollment_id),
                                       auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def voice_verification(self, user_id, lang, phrase, file_path):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        f = open(file_path, 'rb')
        filesObj = [('recording', ('verification.wav', f, 'audio/wav'))]
        try:
            response = requests.post(self.base_URL + '/verification/voice', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def voice_verification_by_url(self, user_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/verification/voice/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def face_verification(self, user_id, file_path, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['doBlinkDetection'] = blink_detection
        f = open(file_path, 'rb')
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/verification/face', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def face_verification_by_url(self, user_id, file_Url, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['fileUrl'] = file_Url
        dataObj['doBlinkDetection'] = blink_detection
        try:
            response = requests.post(self.base_URL + '/verification/face/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_verification(self, user_id, lang, phrase, file_path, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['doBlinkDetection'] = blink_detection
        f = open(file_path, 'rb')
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/verification/video', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def video_verification_by_url(self, user_id, lang, phrase, file_Url, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        dataObj['doBlinkDetection'] = blink_detection
        try:
            response = requests.post(self.base_URL + '/verification/video/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def voice_identification(self, group_id, lang, phrase, file_path):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        f = open(file_path, 'rb')
        filesObj = [('recording', ('identification.wav', f, 'audio/wav'))]
        try:
            response = requests.post(self.base_URL + '/identification/voice', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def voice_identification_by_url(self, group_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/identification/voice/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_identification(self, group_id, lang, phrase, file_path, blink_detection=False):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['doBlinkDetection'] = blink_detection
        f = open(file_path, 'rb')
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/identification/video', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def video_identification_by_url(self, group_id, lang, phrase, file_Url, blink_detection=False):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        dataObj['doBlinkDetection'] = blink_detection
        try:
            response = requests.post(self.base_URL + '/identification/video/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def face_identification(self, group_id, file_path, blink_detection=False):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['doBlinkDetection'] = blink_detection
        f = open(file_path, 'rb')
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/identification/face', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj,
                                     headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def face_identification_by_url(self, group_id, file_Url, blink_detection=False):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['fileUrl'] = file_Url
        dataObj['doBlinkDetection'] = blink_detection
        try:
            response = requests.post(self.base_URL + '/identification/face/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj,
                                     headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

# import hashlib, requests
#
#
# class VoiceIt:
#     developerId = ""
#     urlUsers = 'https://siv.voiceprintportal.com/sivservice/api/users'
#     urlEnrollments = 'https://siv.voiceprintportal.com/sivservice/api/enrollments'
#     urlAuthentication = 'https://siv.voiceprintportal.com/sivservice/api/authentications'
#
#     def getSHA256(self, strData):
#         return hashlib.sha256(strData.encode("ascii")).hexdigest()
#
#     def __init__(self, devId):
#         self.developerId = devId
#
#     def createUser(self, userId, passwd):
#         password = self.getSHA256(passwd)
#         headers = {'PlatformID': '2', 'Content-Type': 'application/json',
#                    "UserId": userId, "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId}
#         try:
#             response = requests.post(self.urlUsers, headers=headers)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def deleteUser(self, userId, passwd):
#         password = self.getSHA256(passwd)
#         headers = {'PlatformID': '2', 'Content-Type': 'application/json',
#                    "UserId": userId,
#                    "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId}
#         try:
#             response = requests.delete(self.urlUsers, headers=headers)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def getUser(self, userId, passwd):
#         password = self.getSHA256(passwd)
#         headers = {'PlatformID': '2', 'Content-Type': 'application/json',
#                    "UserId": userId,
#                    "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId}
#         try:
#             response = requests.get(self.urlUsers, headers=headers)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def createEnrollment(self, userId: object, passwd: object, pathToEnrollmentWav: object,
#                          contentLanguage: object = "") -> object:
#         password = self.getSHA256(passwd)
#
#         with open(pathToEnrollmentWav, 'rb') as file:
#             wavData = file.read()
#
#         headers = {'PlatformID': '2', 'Content-Type': 'audio/wav',
#                    "UserId": userId,
#                    "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId,
#                    "ContentLanguage": contentLanguage}
#         try:
#             response = requests.post(
#                 self.urlEnrollments, headers=headers, data=wavData)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def createEnrollmentByWavURL(self, userId, passwd, urlToEnrollmentWav,
#                                  contentLanguage=""):
#         password = self.getSHA256(passwd)
#         headers = {'PlatformID': '2', 'Content-Type': 'audio/wav',
#                    "UserId": userId, "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId,
#                    "VsitwavURL": urlToEnrollmentWav,
#                    "ContentLanguage": contentLanguage}
#         try:
#             response = requests.post(
#                 self.urlEnrollments + "/bywavurl", headers=headers)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def getEnrollments(self, userId, passwd):
#         password = self.getSHA256(passwd)
#         headers = {'PlatformID': '2', 'Content-Type': 'application/json',
#                    "UserId": userId,
#                    "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId}
#         try:
#             response = requests.get(self.urlEnrollments, headers=headers)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def deleteEnrollment(self, userId, passwd, enrollmentId):
#         password = self.getSHA256(passwd)
#         headers = {'PlatformID': '2', 'Content-Type': 'application/json',
#                    "UserId": userId,
#                    "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId}
#         try:
#             response = requests.delete(
#                 self.urlEnrollments + "/" + enrollmentId, headers=headers)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def authentication(self, userId, passwd, pathToAuthenticationWav,
#                        contentLanguage=""):
#         password = self.getSHA256(passwd)
#
#         with open(pathToAuthenticationWav, 'rb') as file:
#             wavData = file.read()
#
#         headers = {'PlatformID': '2', 'Content-Type': 'audio/wav',
#                    "UserId": userId, "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId,
#                    "ContentLanguage": contentLanguage}
#         try:
#             response = requests.post(
#                 self.urlAuthentication, headers=headers, data=wavData)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()
#
#     def authenticationByWavURL(self, userId, passwd, urlToAuthenticationWav,
#                                contentLanguage=""):
#         password = self.getSHA256(passwd)
#         headers = {'PlatformID': '2', 'Content-Type': 'audio/wav',
#                    "UserId": userId, "VsitPassword": password,
#                    "VsitDeveloperId": self.developerId,
#                    "VsitwavURL": urlToAuthenticationWav,
#                    "ContentLanguage": contentLanguage}
#         try:
#             response = requests.post(
#                 self.urlAuthentication + "/bywavurl", headers=headers)
#             return response.text
#         except requests.exceptions.HTTPError as e:
#             return e.read()