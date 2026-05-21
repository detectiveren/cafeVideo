import sqlite3

# Set the location for the database
cafeDatabasePath = 'cafeDatabase_test.db'


def connect_to_database():
    conn = sqlite3.connect(cafeDatabasePath)
    conn.execute('PRAGMA foreign_keys = ON')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_latest_videos():
    """Fetch videos in the database in descending order"""
    conn = connect_to_database()
    cursor = conn.cursor()

    # Fetch the latest videos for the new videos feed
    cursor.execute("""
                SELECT videos.videoID, accounts.username, videos.videoTitle, videos.views, videos.videoThumbnail, 
                videos.datetime, profiles.profilePicture, profileColorSets.profilePictureBorderColor, 
                profiles.channelURLEnabled, profiles.channelURL
                FROM videos
                JOIN accounts ON videos.userID = accounts.userID
                JOIN profiles ON profiles.userID = accounts.userID
                JOIN profileColorSets ON profiles.profileColorTheme = profileColorSets.profileSetID
                ORDER BY videoID DESC  -- Shows newest first
            """)
    videos = cursor.fetchall()

    return videos


def fetch_profile_info(variant, userID):
    """Fetch the profile of the user from the database"""
    conn = connect_to_database()
    cursor = conn.cursor()

    if variant == "minimal":
        cursor.execute("""
                                SELECT profilePicture, profileColorSets.profilePictureBorderColor, channelURLEnabled, 
                                channelURL
                                FROM profiles 
                                JOIN profileColorSets ON profiles.profileColorTheme = profileColorSets.profileSetID
                                WHERE userID = ?""", (userID,))
        profilePicture = cursor.fetchone()

        return profilePicture


def fetch_subscription_info(userID):
    """Fetches the user subscriptions from the database"""
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("""
                            SELECT profilePicture, profileColorSets.profilePictureBorderColor, accounts.userID, 
                            accounts.username, channelURLEnabled, channelURL
                            FROM profiles
                            JOIN accounts ON profiles.userID = accounts.userID
                            JOIN profileColorSets ON profiles.profileColorTheme = profileColorSets.profileSetID
                            JOIN subscriptions ON subscriptions.subscribedToUserID = accounts.userID
                            WHERE subscriptions.userID = ?""", (userID,))
    subscriptionsInfo = cursor.fetchall()

    return subscriptionsInfo


def fetch_subscription_videos(variant, userID):
    """Fetches the user subscription videos from the database"""
    conn = connect_to_database()
    cursor = conn.cursor()

    if variant == "latest":
        cursor.execute("""
                                SELECT videos.videoID, accounts.username, videos.videoTitle, videos.views, 
                                videos.videoThumbnail, videos.datetime, profiles.profilePicture, 
                                profileColorSets.profilePictureBorderColor, profiles.channelURLEnabled, profiles.channelURL
                                FROM videos
                                JOIN accounts ON videos.userID = accounts.userID
                                JOIN profiles ON profiles.userID = accounts.userID
                                JOIN profileColorSets ON profiles.profileColorTheme = profileColorSets.profileSetID
                                JOIN subscriptions ON subscriptions.subscribedToUserID = accounts.userID
                                WHERE subscriptions.userID = ?
                                ORDER BY videoID DESC  -- Shows newest first
                                LIMIT 12
                                """, (userID,))
        subscription_videos = cursor.fetchall()

        return subscription_videos


def fetch_user_notifications(variant, userID):
    """Fetch user notifications from the database"""
    conn = connect_to_database()
    cursor = conn.cursor()

    if variant == "minimal":
        cursor.execute("""
                                SELECT notifications.*, profiles.profilePicture, profileColorSets.profilePictureBorderColor 
                                FROM notifications
                                JOIN profiles ON notifications.notificationSenderID = profiles.userID
                                JOIN profileColorSets ON profiles.profileColorTheme = profileColorSets.profileSetID
                                WHERE notificationRecipientID = ?
                                ORDER BY notificationDateTime DESC
                                         """,
                       (userID,))
        notifications = cursor.fetchall()

        return notifications


def fetch_account_info(variant, userID):
    """Fetch the user account info from the database"""
    conn = connect_to_database()
    cursor = conn.cursor()

    if variant == "feature_access":
        cursor.execute("""
                                SELECT feature_access.featureID, feature_gating.featureName
                                FROM feature_access
                                JOIN feature_gating ON feature_access.featureID = feature_gating.featureID
                                JOIN accounts ON feature_access.userID = accounts.userID
                                WHERE accounts.userID = ?  
                                """, (userID,))
        featureAccess = cursor.fetchall()

        return featureAccess
