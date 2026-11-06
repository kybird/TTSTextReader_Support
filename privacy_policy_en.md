# TTSTextViewer Privacy Policy

TTSTextViewer (hereinafter "the App") takes user privacy seriously and complies with applicable laws. This policy clearly discloses what information is collected within the App and how it is used.

---

## 1. Information We Collect and How We Collect It

The App collects minimal information necessary to provide its services.

- **Advertising Identifier (AD_ID / IDFA)**: May be collected for displaying in-app banner ads and providing personalized advertising.
- **In-App Purchase Information**: When purchasing subscription products (ad removal), receipt information from Google Play / Apple App Store is referenced to verify payment status. (Financial information such as card numbers is not directly collected.)
- **Device Information**: Device model name, OS version, etc. may be collected for app troubleshooting and optimization.
- **App Settings and Usage Records**: App settings, bookmarks, last reading position, premium subscription status, etc. are stored in the device's local storage for user convenience. (Not transmitted to a server.)

## 2. Purpose of Personal Information Use

- **Ad Display**: Providing banner ads through Google AdMob
- **Subscription Service**: Verifying payment status and activating features for the 'Background Playback + Ad Removal' premium product
- **Service Improvement**: Error analysis and feature enhancement

## 3. Third-Party Services and Data Sharing

The App utilizes the following professional services for smooth service provision:

- **Google AdMob**: Ad display and tracking (in compliance with Google AdMob policies)
- **Google Play Billing / Apple In-App Purchase**: In-app purchase processing and management
- **Firebase**: App analytics and crash report collection (Analytics, Crashlytics)
- **HuggingFace (huggingface.co)**: Downloading high-quality AI TTS voice synthesis models (only when the user chooses to download models)
- **Gutendex / Project Gutenberg**: Public domain book search, catalog browsing, cover display, and book downloads. Search terms entered by the user and selected language/subject filters are transmitted to Gutendex, and book files are downloaded from the respective download server to the device.
- **Wikisource (wikisource.org)**: Multilingual public literature search and full-text download from the Wikimedia Foundation. Search terms entered by the user and selected language edition (ko/en/zh/ja/es/fr) are transmitted to the corresponding language's Wikisource server (`{lang}.wikisource.org`), and the selected work's full text (HTML) is downloaded to the device, converted to plain text, and saved.
- **Aozora Bunko (www.aozora.gr.jp)**: Japanese classical literature archive. The work catalog (CSV, approximately 2MB) is downloaded upon first access and cached on the device; subsequent search and category filtering are performed offline on the device. The full text (Shift_JIS encoded zip) of works the user chooses to download is downloaded to the device, converted to UTF-8, and saved. All works are in the public domain.
- **Operating System TTS Provider**: When the user selects a system voice, the text to be read is transmitted to the operating system's TTS service (Android, iOS, etc.). Whether processing is on-device or online depends on the selected system voice, OS settings, and provider policies.

## 4. Advertising and Subscription Policies

- **Banner Ads**: Google AdMob banner ads are displayed in some parts of the App.
- Ads are served according to Google AdMob default settings, and users can opt out of personalized advertising through OS settings.
- **Ad-Free Subscription**: When a user purchases a premium subscription, background playback is activated, all banner ads are removed, and benefits are maintained for the duration of the subscription.

## 5. Data Retention and Disposal

- The App does not directly store users' sensitive personal information on a server.
- Advertising identifiers and payment tokens are managed according to each operating system's (Android/iOS) and store's policies.
- When a user deletes the App or discontinues service, collected advertising identifier information is immediately invalidated.
- App settings, bookmarks, and other locally stored data are kept only on the device and deleted when the App is uninstalled.
- AI voice synthesis model files are downloaded to device storage and can be deleted by the user or by uninstalling the App.
- Book files downloaded from Project Gutenberg and library information are stored on the device and removed when the user deletes them from the App or uninstalls the App.
- Text files downloaded from Wikisource are similarly stored on the device and removed when the user deletes them or uninstalls the App.
- Aozora Bunko work catalog cache and downloaded work text files are also stored on the device and removed when the user deletes them or uninstalls the App.
- **Text Processing**: When using the App's local AI voices, document content is processed within the device. When using system voices, processing methods follow the operating system's TTS settings and provider policies.
- **Voice Cloning Audio Processing**: In the 'Create My Voice' feature, recorded or imported audio (microphone recording/WAV file) is analyzed on-device only, and only the analysis result (voice characteristics) is stored on the device. Original audio files are not transmitted to or stored on a server. Microphone permission is requested only when using the feature. Created voices can be deleted within the App or are removed when the App is uninstalled.

## 6. User Rights and Opt-Out Methods

Users can refuse or withdraw consent to personal information collection at any time through OS settings:
- **Android**: Settings > Google > Ads > Opt out of Ads Personalization
- **iOS**: Settings > Privacy & Security > Tracking > Turn off Allow App to Track

## 7. Account and Data Deletion

Users can request deletion of their account and related data at any time.

- **In-app deletion**: Settings > Account Management > Delete Account
- **Email request**: Request account deletion via kybirdlabs@gmail.com
- **Deletion guide page**: https://kybird.github.io/TTSTextReader_Support/account-deletion.html (available without the App)

Upon deletion request, account information, subscription status, and user data stored in Firestore are permanently deleted.

## 8. Contact

For questions about this policy, please contact:

- **Team**: kybirdlabs Development Team
- **Email**: kybirdlabs@gmail.com

---
**Last Updated**: October 15, 2026
