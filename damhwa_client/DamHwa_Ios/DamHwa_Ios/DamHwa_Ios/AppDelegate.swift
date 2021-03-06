//
//  AppDelegate.swift
//  DamHwa_Ios
//
//  Created by minkpang on 2021/09/28.
//

import SwiftUI
import KakaoSDKCommon
import KakaoSDKAuth
import Firebase

class AppDelegate: NSObject, UIApplicationDelegate{
    
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
        
        KakaoSDKCommon.initSDK(appKey: "5d4ceabed4218c89d458e28bfdd4ed60", loggingEnable:false)
        FirebaseApp.configure()

        return true
    }
    
    func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
           if (AuthApi.isKakaoTalkLoginUrl(url)) {
               return AuthController.handleOpenUrl(url: url, options: options)
           }
           
           return false
       }

}
