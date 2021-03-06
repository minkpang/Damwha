# ๐ ํ๋ก์ ํธ์์ ์ฌ์ฉํ๋ ์ธ๋ถ์๋น์ค ์ ๋ณด ๋ฌธ์

์ฌ์ฉํ ์ ๋ณด ๋ฌธ์: ์นด์นด์ค ์์ ๋ก๊ทธ์ธ, ์นด์นด์คํก ๊ณต์ , Apple Login

### ๐ ์นด์นด์ค ์์ ๋ก๊ทธ์ธ

- ์๋๋ก์ด๋ Kotlin ๋ฐ ios Swift ์์ ์นด์นด์ค ์์ ๋ก๊ทธ์ธ ๊ตฌํ
- ์์ ๋ก๊ทธ์ธ์ ๊ตฌํํ๊ธฐ ์ํด ์นด์นด์ค ๊ฐ๋ฐ์ ํ์ด์ง์์ ์ฑ ๋ฑ๋ก ๋ฐ API key๊ฐ ์์ฑ
- ์นด์นด์ค์ ๋ก๊ทธ์ธ ํ AccessToken์ผ๋ก ์นด์นด์ค์ ๋ฑ๋ก๋ ํ์์ ์ ๋ณด๋ฅผ ๋ฐ์์ DB์ ์ ์ฅ

##### ๐ธ ์๋๋ก์ด๋ ์นด์นด์ค ํก ๋ก๊ทธ์ธ ๊ตฌํ ๋ฐฉ๋ฒ

1. `kakao developer์ ์` โ `login` โ `my application` โ `์๋น์ค ํ๋ซํผ url ๋ฐ package ๋ฑ๋ก`

2. ์๋๋ก์ด๋ ์คํ๋์ค build.gradle(module) โ ํ์ `dependencies` ์๋์ ๊ฐ์ด ์ถ๊ฐ

   ```kotlin
   // ์์ ๋ก๊ทธ์ธ ์นด์นด์ค
   def kakaoLoginVersion = "2.8.1"
   implementation "com.kakao.sdk:v2-user:$kakaoLoginVersion" // ์นด์นด์ค ๋ก๊ทธ์ธ
   implementation "com.kakao.sdk:v2-user-rx:$kakaoLoginVersion"
   implementation "com.kakao.sdk:v2-link:$kakaoLoginVersion" // ์นด์นด์ค ๋งํฌ / ์๋ ์นด์นด์ค ๋งํฌ๋ฅผ ์ํ ๋ํ๋์
   implementation "com.kakao.sdk:v2-link-rx:$kakaoLoginVersion"
   ```

3. ์นด์นด์ค ํ๋ซํผ ํค ์ ์ญ ๋ณ์ ์ค์ 

   ```kotlin
   package com.example.damhwa_android.constants
   
   object Constants {
       const val KAKAO_KEY = "๋ฐ์ ์นด์นด์คํค ๋ฑ๋ก"
   }
   ```

4. ์นด์นด์ค SDK ์ค์  damhwa_android ํจํค์ง ๋ด์ `Globalapplication.kt` ํ์ผ ์์ฑ ๋ฐ ์ฝ๋ ์์ฑ

   ```kotlin
   import android.app.Application
   import com.example.damhwa_android.constants.Constants.KAKAO_KEY // 3๋ฒ์ kakao key๋ฅผ ์ฌ๊ธฐ์ ์ด์ฉ
   import com.example.damhwa_android.data.sharedpreferences.DamhwaSharedPreferencesImpl
   import com.kakao.sdk.common.KakaoSdk
   
   
   class GlobalApplication : Application() {
       override fun onCreate() {
           super.onCreate()
           initializeKakaoSDK()
           initializeSharedPreferences()
       }
   
       private fun initializeKakaoSDK() {
           KakaoSdk.init(this, KAKAO_KEY)
       }
   
       private fun initializeSharedPreferences() {
           DamhwaSharedPreferencesImpl.init(this)
       }
   }
   ```

5. `AndroidManifest.xml`ํ์ผ์์ android:name=".GlobalApplication" ์ค์ 

   ```xml
   <application
                ...
           android:name=".GlobalApplication"
                ...
   </application>
   ```

6. ์นด์นด์ค ํค๊ฐ์ xml์์ ํ์ฉํ๊ธฐ ์ํด์ values์ strings.xml์์ ์ด๋ฅผ ์ถ๊ฐ

   ```xml
   <string name="kakao_app_key">์ฌ๊ธฐ์ ์นด์นด์คํค๋ฅผ ์๋ ฅํด์ฃผ์ธ์</string> 
   ```

   ์ด์  ์์ `kakao_app_key`๋ฅผ `xml`์์ ์ฌ์ฉํ  ๊ฒ์

7. ์ดํ ๋ค์ `AndroidManifest.xml`ํ์ผ์์ kakao_app_key๋ฅผ ์ฌ์ฉ

   ```xml
   <activity
   	...
   
       <data
        android:host="oauth"
        android:scheme="@string/kakao_app_key" />
   	...
   </activity>
   ```

8. ์ดํ ์๋์ ๊ฐ์ด ๋ก๊ทธ์ธ์ด ์ผ์ด๋๋ activity.ktํ์ผ์์ ์นด์นด์ค ์ฌ์ฉ์ ์์ฒญ์ ๋ณด๋ด๋ฉด ๋๋ค.

   ```kotlin
   // fragment์์ ์นด์นด์ค ๋ก๊ทธ์ธํ๊ธฐ
   override fun init() {
           super.init()
           binding.kakaoLoginButton.setOnClickListener {
                     kakaoLogin()
           }
   }
   
   private fun kakaoLogin() {
           Single.just(UserApiClient.instance.isKakaoTalkLoginAvailable(requireContext()))
               .flatMap { available ->
                   if (available) UserApiClient.rx.loginWithKakaoTalk(requireContext())
                   else UserApiClient.rx.loginWithKakaoAccount(requireContext())
               }
               .observeOn(AndroidSchedulers.mainThread())
               .subscribe({ token ->
                   getUserInfo()
                   Log.i(TAG, "๋ก๊ทธ์ธ ์ฑ๊ณต ${token.accessToken}")
               }, { error ->
                   Log.e(TAG, "๋ก๊ทธ์ธ ์คํจ", error)
               })
               .addToDisposable()
       }
   
   private fun getUserInfo() {
           UserApiClient.rx.me()
               .subscribeOn(Schedulers.io())
               .observeOn(AndroidSchedulers.mainThread())
               .subscribe({ user ->
                   landingViewModel.login(
                       userNo = user.id,
                       username = user.kakaoAccount?.profile?.nickname,
                       email = user.kakaoAccount?.email,
                       profile = user.kakaoAccount?.profile?.thumbnailImageUrl
                   )
               }, { error ->
                   Log.e(TAG, "์ฌ์ฉ์ ์ ๋ณด ์์ฒญ ์คํจ", error)
               })
               .addToDisposable()
       }
   
   private fun Disposable.addToDisposable(): Disposable = addTo(disposables)
   ```

   ์ฝํ๋ฆฐ ์นด์นด์ค ์์ ๋ก๊ทธ์ธ ๋

### ๐ ์นด์นด์คํก ๊ณต์ 

- ๊ธฐ๋ณธ ํํ๋ฆฟ์ผ๋ก ์นด์นด์ค ๋งํฌ๋ฅผ ์นด์นด์คํก์ผ๋ก ๋ณด๋๋๋ค.
- ์ด๋ ๋ฉ์ธ์ง๋ jsonํ์์ ํ์ผ๋ก ๋ณด๋ด์ง๊ฒ ๋ฉ๋๋ค.
- ์นด์นด์คํก์ ํตํด ๋ฉ์์ง ๊ณต์ ๊ฐ ๊ฐ๋ฅํ์ง ํ์ธํ๊ธฐ ์ํด ๋จผ์  `isKakaoLinkAvailable`๋ฅผ ํธ์ถํ์ฌ ์ฌ์ฉ์ ๊ธฐ๊ธฐ์ ์นด์นด์คํก์ด ์ค์น๋์ด ์๋์ง ํ์ธํฉ๋๋ค.
- ์นด์นด์คํก์ด ์ค์น๋์ด ์๋ ๊ฒฝ์ฐ `defaultTemplate`๋ฅผ ํธ์ถํ์ฌ ์นด์นด์คํก์ผ๋ก ๋ฉ์์ง๋ฅผ ๊ณต์ ํ  ์ ์๋๋ก ํฉ๋๋ค.
- ์นด์นด์คํก์ด ์ค์น๋์ด ์์ง ์๋ค๋ฉด `WebSharerClient`์ `defaultTemplateUri`๋ฅผ ํตํด ๊ณต์ ์ฉ URL์ ์ ์ธํ ํ, ๊ธฐ๋ณธ ๋ธ๋ผ์ฐ์ ๋ ์น๋ทฐ๋ก ํด๋น URL์ ์ด ์ ์๋๋ก ๊ตฌํํฉ๋๋ค.

##### ๐ต ์๋๋ก์ด๋ ์นด์นด์ค ๋งํฌ ๊ณต์ ํ๊ธฐ ๊ตฌํ

```kotlin
package com.kakao.sdk.common.util

import android.content.*
import android.content.pm.PackageManager
import android.net.Uri
import androidx.browser.customtabs.CustomTabsClient
import androidx.browser.customtabs.CustomTabsIntent
import androidx.browser.customtabs.CustomTabsService
import androidx.browser.customtabs.CustomTabsServiceConnection

/**
 * ๊ฐํธํ CustomTabs ์คํ ๊ธฐ๋ฅ์ ์ ๊ณตํฉ๋๋ค.
 */
object KakaoCustomTabsClient {

    @Throws(UnsupportedOperationException::class)
    fun openWithDefault(context: Context, uri: Uri): ServiceConnection? {
        val packageName = resolveCustomTabsPackage(
            context,
            uri
        ) ?: throw UnsupportedOperationException()
        SdkLog.d("Choosing $packageName as custom tabs browser")
        val connection = object : CustomTabsServiceConnection() {
            override fun onCustomTabsServiceConnected(name: ComponentName?, client: CustomTabsClient?) {
                val builder = CustomTabsIntent.Builder()
                        .enableUrlBarHiding().setShowTitle(true)
                val customTabsIntent = builder.build()
                customTabsIntent.intent.data = uri
                customTabsIntent.intent.setPackage(packageName)
                context.startActivity(customTabsIntent.intent)
            }

            override fun onServiceDisconnected(name: ComponentName?) {
                SdkLog.d("onServiceDisconnected: $name")
            }
        }
        val bound = CustomTabsClient.bindCustomTabsService(context, packageName, connection)
        return if (bound) connection else null
    }

    @Throws(ActivityNotFoundException::class)
    fun open(context: Context, uri: Uri) {
        CustomTabsIntent.Builder().enableUrlBarHiding().setShowTitle(true).build()
                .launchUrl(context, uri)
    }

    private fun resolveCustomTabsPackage(context: Context, uri: Uri): String? {
        var packageName: String? = null
        var chromePackage: String? = null
        // get ResolveInfo for default browser
        val intent = Intent(Intent.ACTION_VIEW, uri)
        val resolveInfo = context.packageManager.resolveActivity(intent, PackageManager.MATCH_DEFAULT_ONLY)
        val serviceIntent = Intent().setAction(CustomTabsService.ACTION_CUSTOM_TABS_CONNECTION)
        val serviceInfos = context.packageManager.queryIntentServices(serviceIntent, 0)
        for (info in serviceInfos) {
            // check if chrome is available on this device
            if (chromePackage == null && isPackageNameChrome(
                    info.serviceInfo.packageName
                )
            ) {
                chromePackage = info.serviceInfo.packageName
            }
            // check if the browser being looped is the default browser
            if (info.serviceInfo.packageName == resolveInfo?.activityInfo?.packageName) {
                packageName = resolveInfo?.activityInfo?.packageName
                break
            }
        }
        if (packageName == null && chromePackage != null) {
            packageName = chromePackage
        }
        return packageName
    }

    private fun isPackageNameChrome(packageName: String): Boolean {
        return chromePackageNames.contains(packageName)
    }

    private val chromePackageNames = arrayOf(
            "com.android.chrome",
            "com.chrome.beta",
            "com.chrome.dev")
}
```



### ๐ Apple Login

-
