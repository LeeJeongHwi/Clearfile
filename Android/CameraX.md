# CameraX Tutorial

* 선수지식
  * 기본 안드로이드 개발 지식
* CameraX 사용처
  * 실시간 카메라 프레임 분석
  * 사진 저장
* 실행 환경
  * Minimum Support API Level : 21
  * Android Studio - ver 3.6 이상
  * Android 11 이상의 디바이스 및 Emulator



## CameraX Life Cycle

CameraX는 카메라를 열 때, 캡쳐 세션을 생성할 때, 기능을 중지시키고 shut down 시킬 때를 결정하기 위한 Life Cycle을 따른다.

그때 사용하는 메서드, 콜백등을 Dependency에 추가해야한다.

> **View Class**
>
> "View"는 앱에서 가시적으로 표현되는 모든 것들을 가리킴 ex) 버튼, 이미지, 테이블, 레이블 등등...
>
> View Class를 베이스로 두고 이 클래스를 상속받는 각각의 기능의 뷰들이 탄생하는 것
>
> View Class는 모든 View들의 부모 클래스이다.
>
> 여기서 ViewGroup Class랑 View Class랑 나뉘어지는데, View 계열의 Class는 가시적으로 모양이 있는 클래스이다.
>
> ViewGroup Class는 눈에는 보이지 않지만 View들을 배치하거나 Grouping 하는 역할을 하게 된다.
>
> 따라서 ViewGroup 클래스는 View들을 담는 컨테이너 역할을 한다. 하지만 ViewGroup또한 View 를 상속받는다.



## Android Context

Context - 애플리케이션의 현재 상태의 맥락을 의미, 새로 생성된 객체가 지금 어떤 일이 일어나고 있는지 알 수 있도록 함

액티비티와 애플리케이션에 대한 정보를 얻기 위해서는 컨텍스트를 사용하면 됨

디바이스 내의 여러 리소스 등의 대한 접근 방법을 제공함

#### Application Context

* Singleton 객체
* Activity Level에서 `getApplicationContext()` 메소드를 통해 접근이 가능함
* 현재 컴포넌트의 Context와 분리된 라이프 사이클을 가진 Context가 필요할 때, 혹은 그 Context에 뭔가를 전달할 때 사용
* ex) 라이브러리를 초기화 하는 경우에는 애플리케이션 컨텍스트를 전달

#### Activity Context

* Activity 의 Life Cycle과 고나련있는 컨텍스트, 액티비티 레벨에서 컨텍스트를 전달할 때 사용
* ex) 액티비티에 뷰를 붙일 때 액티비티 컨텍스트를 사용





## CameraX Tutorial Code

[Android CameraX Tutorial](https://codelabs.developers.google.com/codelabs/camerax-getting-started?hl=ko#1)

#### 1. Add the Gradle Dependencies

* `build.gradle(Module: App)` 파일에서 dependencies에 해당 section을 추가해준다.
* Life Cycle 시점을 결정하기 위한 Dependency이다.

```groovy
def camerax_version = "1.0.0-beta07"
// CameraX core library using camera2 implementation
implementation "androidx.camera:camera-camera2:$camerax_version"
// CameraX Lifecycle Library
implementation "androidx.camera:camera-lifecycle:$camerax_version"
// CameraX View class
implementation "androidx.camera:camera-view:1.0.0-alpha14"
```

* CameraX 는 java 8 버전 이상에 쓰임, 따라서 Compile Option을 확인해볼 것

```groovy
compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
}
```

* 그리고 plugin을 추가한다.

```groovy
plugins {
    id 'com.android.application'
    id 'kotlin-android'
    id 'kotlin-android-extensions' //add Plugin
}
```



#### 2. Create the viewfinder layout

* `main Layout` 생성

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
   xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:tools="http://schemas.android.com/tools"
   xmlns:app="http://schemas.android.com/apk/res-auto"
   android:layout_width="match_parent"
   android:layout_height="match_parent"
   tools:context=".MainActivity">

   <Button
       android:id="@+id/camera_capture_button"
       android:layout_width="100dp"
       android:layout_height="100dp"
       android:layout_marginBottom="50dp"
       android:scaleType="fitCenter"
       android:text="Take Photo"
       app:layout_constraintLeft_toLeftOf="parent"
       app:layout_constraintRight_toRightOf="parent"
       app:layout_constraintBottom_toBottomOf="parent"
       android:elevation="2dp" />

   <androidx.camera.view.PreviewView
       android:id="@+id/viewFinder"
       android:layout_width="match_parent"
       android:layout_height="match_parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

* Button과 CameraX의 Preview로 구성되어있는 MainActivity

#### 3. Set up MainActivity.kt

* `MainActivity.kt` 내부 코드이다.

* import 부터 살펴보자
  * `androidx.appcompat.app.AppCompatActivity`
    * 이전 Android 기기에서 최신 플랫폼 기능을 사용하기 위한 기본 클래스
  * `android.content.pm.PackageManager`
    * 장치에 현재 설치되어 있는 응용프로그램 패키지와 관련된 다양한 정보를 검색하는 클래스
  * `android.widget.Toast`
    * 빠르고 짧은 메시지를 사용자에게 보여주는 view
  * `androidx.core.app.ActivityCompat`
    * Activity 내에 있는 기능들을 Access 하는 것을 도와주는 클래스
  * `androidx.core.content.ContextCompat`
    * Context 내에있는 기능들을 Access 하는 것을 도와주는 클래스
  * `java.util.concurrent.Executors`
    * 인자로 전달된 `Runnable` Task를 실행시키는 객체이다.
    * Thread 사용, 스케쥴링 등의 세부정보를 포함하여 각 작업이 실행되는 메커니즘 등을 decoupling 하는 방법을 제공해주는 인터페이스

  * `androidx.camera.lifecycle.ProcessCameraProvider`
    * 애플리케이션의 프로세스내에서 Camera Life Cycle -> LifeCycleOwner에 바인딩 하는데 사용할 수 있는 싱글톤
  * `java.util.concurrent.ExecutorService`
    * 하나 이상의 비동기 작업의 진행률을 추적하기 위한 `Future`를 생성하는 메소드와 종료 메소드를 관리하기 위한 메소드를 제공해주는 실행자

```kotlin
package com.example.camerax_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.Manifest
import android.content.pm.PackageManager
import android.net.Uri
import android.util.Log
import android.widget.Toast
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import java.util.concurrent.Executors
import androidx.camera.core.*
import androidx.camera.lifecycle.ProcessCameraProvider
import kotlinx.android.synthetic.main.activity_main.*
import java.io.File
import java.nio.ByteBuffer
import java.text.SimpleDateFormat
import java.util.*
import java.util.concurrent.ExecutorService
typealias LumaListener = (luma: Double) -> Unit

class MainActivity : AppCompatActivity() {
    private var imageCapture : ImageCapture? = null

    private lateinit var outputDirectory : File
    private lateinit var cameraExecutor : ExecutorService

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Request Camera Permissions
        if (allPermissionsGranted()){
            startCamera()
        }else{
            ActivityCompat.requestPermissions(
                    this, REQUIRED_PERMISSIONS,REQUEST_CODE_PERMISSIONS
            )
        }

        // Set up the listener for take photo button
        camera_capture_button.setOnClickListener{takePhoto()}
        outputDirectory = getOutputDirectory()
        cameraExecutor = Executors.newSingleThreadExecutor()
    }
    private fun takePhoto() {}
    private fun startCamera() {}
    private fun allPermissionsGranted() = REQUIRED_PERMISSIONS.all {
        ContextCompat.checkSelfPermission(
                baseContext, it) == PackageManager.PERMISSION_GRANTED
    }
    private fun getOutputDirectory(): File{
        val mediaDir = externalMediaDirs.firstOrNull()?.let{
            File(it, resources.getString(R.string.app_name)).apply {mkdirs()}
        }
        return if (mediaDir != null && mediaDir.exists())
            mediaDir else filesDir
    }

    override fun onDestroy() {
        super.onDestroy()
        cameraExecutor.shutdown()
    }
    companion object{
        private const val TAG = "CameraXBasic"
        private const val FILENAME_FORMAT = "yyyy-MM-dd-HH-mm-ss-SSS"
        private const val REQUEST_CODE_PERMISSIONS = 10
        private val REQUIRED_PERMISSIONS = arrayOf(Manifest.permission.CAMERA)
    }
}
```

* `companion object`
  * 전역변수 선언과 같은 역할을 함

#### Request Camera Permissions

* 카메라 앱을 열기 전에 permissions 허용이 되어야한다. 
* `AndroidManifest.xml` 파일 `application` 태그 전에 해당 태그를 붙여주자
  * 카메라에 앱이 접근할 수 있도록 권한을 주는 코드와 카메라가 달려있음을 확인하는 코드 (Any는 앞 뒤 카메라 중 하나만 있어도 됨)

```xml
<uses-feature android:name="android.hardware.camera.any" />
<uses-permission android:name="android.permission.CAMERA" />
```

* `MainActivity.kt`에 Request Permission을 처리하는 함수를 Override 한다.

```kotlin
override fun onRequestPermissionsResult(
   requestCode: Int, permissions: Array<String>, grantResults:
   IntArray) {
   if (requestCode == REQUEST_CODE_PERMISSIONS) {
       if (allPermissionsGranted()) {
           startCamera()
       } else {
           Toast.makeText(this,
               "Permissions not granted by the user.",
               Toast.LENGTH_SHORT).show()
           finish()
       }
   }
}
```

* 권한 요청에 관한 Kotlin 코드이다.
* 권한 부여가 되면 `startCamera` 함수를 실행시키고, 그렇지 않으면 부여되지 않았다는 메시지 출력

* `ActivityCompat`의 콜백 메소드로서 요청한 권한에 대한 결과를 받는 접점과 관련된 인터페이스

#### Implement Preview use Case

* CameraX `Preview` Class를 사용해서 `ViewFinder`를 구현한다.
  * 유저들이 찍을 사진을 미리 보여주는 역할
* 우선 useCase Instance를 만들기 위한 `configuration`를 정의해야한다. 결과 instance는 CameraX LifeCycle과 Binding 됨

```kotlin
//startCamera Function
private fun startCamera() {
   val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
    
   cameraProviderFuture.addListener(Runnable {
       // Used to bind the lifecycle of cameras to the lifecycle owner
       val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()

       // Preview
       val preview = Preview.Builder()
          .build()
          .also {
              it.setSurfaceProvider(viewFinder.createSurfaceProvider())
          }

       // Select back camera as a default
       val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA

       try {
           // Unbind use cases before rebinding
           cameraProvider.unbindAll()

           // Bind use cases to camera
           cameraProvider.bindToLifecycle(
               this, cameraSelector, preview)

       } catch(exc: Exception) {
           Log.e(TAG, "Use case binding failed", exc)
       }

   }, ContextCompat.getMainExecutor(this))
}
```

```kotlin
val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
```

* `ProcessCameraProvider` 의 `getInstance` 함수로 Instance를 생성한다.
  * 카메라 life Cycle을 life Cycle 소유자(MainActivity에게 바인딩하는데 사용
  * CameraX는 Life cycle을 인식해서 카메라를 열고 닫는 작업이 제거됨 (카메라 앱을 이야기하는 것 같음)

```kotlin
cameraProviderFuture.addListener(Runnable {}, ContextCompat.getMainExecutor(this))
```

* `cameraProviderFuture` 인스턴스에 리스너를 추가한다.
* `Runnaable` , `ContextCompat.getMainExecutor()` 를 인자로 준다
  * `Runnable`은 Thread를 생성하는 인터페이스, 해당 인터페이스를 구현하는 클래스의 인스턴스는 쓰레드에 의해 실행될 목적으로 구현되어야 함
  * `Executor`는 `Runnable Task`를 수행한다.
  * `ContextCompat.getMainExecutor()`는 `MainActivity:AppCompatActivity()` 의 컨텍스트를 입력 받아서 `Main Thread` 에서 돌아가는 `Executor`를 리턴함

```kotlin
val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()
```

* `ProcessCameraProvider`를 추가한다. 이것은  카메라의 라이프 사이클을 애플리케이션 프로세스내에서 
  Life Cycle Owner(`MainActivity:AppCompatAcitivty()`)와 바인딩 하기 위해서 사용된다.



```kotlin
val preview = Preview.Builder()
   .build()
   .also {
       it.setSurfaceProvider(viewFinder.createSurfaceProvider())
   }
```

* `Preview` Object를 초기화하고, Build 메소드를 호출하고 `ViewFinder`에서 `Surface provider`를 얻은 뒤에 그걸 `preview` 에 Set 해준다.

```kotlin
val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
```

* `CameraSelector` 객체를 만들고 `DEFAULT_BACK_CAMERA` , 즉 후면 카메라를 카메라로 선택한다.

```kotlin
try {
   cameraProvider.unbindAll()
   cameraProvider.bindToLifecycle(
       this, cameraSelector, preview)
}catch(exc:Exception){
    Log.e(TAG,"Use case binding Failed",exc)
}
```

* `CameraProvider`가 바인딩 된 것이 없는지 확인하고, `CameraSelector`와 `Preview` 객체를 `CameraProvider` 에 바인딩한다.
* 바인딩이 실패하면 Catch문 발생



#### Implement ImageCapture use case

다른 use Cases (=기능) 들도 `Preview` 방식과 비슷하게 동작한다.

1. 구성요소 설정
2. 바인딩

```kotlin
private fun takePhoto() {
   // Get a stable reference of the modifiable image capture use case
   val imageCapture = imageCapture ?: return

   // Create time-stamped output file to hold the image
   val photoFile = File(
       outputDirectory,
       SimpleDateFormat(FILENAME_FORMAT, Locale.US
       ).format(System.currentTimeMillis()) + ".jpg")

   // Create output options object which contains file + metadata
   val outputOptions = ImageCapture.OutputFileOptions.Builder(photoFile).build()

   // Set up image capture listener, which is triggered after photo has
   // been taken
   imageCapture.takePicture(
       outputOptions, ContextCompat.getMainExecutor(this), object : ImageCapture.OnImageSavedCallback {
           override fun onError(exc: ImageCaptureException) {
               Log.e(TAG, "Photo capture failed: ${exc.message}", exc)
           }

           override fun onImageSaved(output: ImageCapture.OutputFileResults) {
               val savedUri = Uri.fromFile(photoFile)
               val msg = "Photo capture succeeded: $savedUri"
               Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
               Log.d(TAG, msg)
           }
       })
}
```

```kotlin
val imageCapture = imageCapture ?: return
```

* Class 에 선언된 `imageCapture` 가 null이라면 아직 set up이 되어있지 않다는 뜻이므로 `return` 한다.

```kotlin
val photoFile = File(
   outputDirectory,
   SimpleDateFormat(FILENAME_FORMAT, Locale.US
   ).format(System.currentTimeMillis()) + ".jpg")
```

* `time stamp` 을 file name에 더해서 고유한 파일이름을 가지게 한다.

```kotlin
val outputOptions = ImageCapture.OutputFileOptions.Builder(photoFile).build()
```

* `OutputFileOptions` 객체를 생성한다.
  * 이 객체는 원하는 출력방식에 대한 정보를 저장하고 위에 만든 PhotoFile에 출력을 저장하려는 경우 사진 파일 을 추가

```kotlin
imageCapture.takePicture(
   outputOptions, ContextCompat.getMainExecutor(this), object : ImageCapture.OnImageSavedCallback {} 
)
```

* `takePicture()` 함수에 `outputOptions`와 `Executor` 와 이미지 저장될 때 실행되는 콜백함수를 넘긴다.

```kotlin
override fun onError(exc: ImageCaptureException) {
   Log.e(TAG, "Photo capture failed: ${exc.message}", exc)
}
```

* 이미지 캡쳐 실패 혹은 캡쳐파일을 저장하는 것이 실패하면 error

```kotlin
override fun onImageSaved(output: ImageCapture.OutputFileResults) {
   val savedUri = Uri.fromFile(photoFile)
   val msg = "Photo capture succeeded: $savedUri"
   Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
   Log.d(TAG, msg)
}
```

* 캡쳐가 성공하면 전에 내가 만들어두었던 파일에 사진을 저장한다. 그리고 성공했다고`Toast`로 알린다.
* 마지막으로 성공로그 출력

```kotlin
cameraProvider.bindToLifecycle(
   this, cameraSelector, preview, imageCapture)
```

* `startCamera()` 함수에서 바인딩을 업데이트 한다.



#### Image Analysis use Case (Luminosity)

* 평균 광도를 분석하는 기능을 만든다.

```kotling
private class LuminosityAnalyzer(private val listener: LumaListener) : ImageAnalysis.Analyzer {

   private fun ByteBuffer.toByteArray(): ByteArray {
       rewind()    // Rewind the buffer to zero
       val data = ByteArray(remaining())
       get(data)   // Copy the buffer into a byte array
       return data // Return the byte array
   }

   override fun analyze(image: ImageProxy) {

       val buffer = image.planes[0].buffer
       val data = buffer.toByteArray()
       val pixels = data.map { it.toInt() and 0xFF }
       val luma = pixels.average()

       listener(luma)

       image.close()
   }
}
```

* inner 클래스로 `LuminosityAnalyzer` 클래스를 만들었다. 
* `rewind()` : 버퍼를 0으로 만든다.
* data

```kotlin
val imageAnalyzer = ImageAnalysis.Builder()
   .build()
   .also {
       it.setAnalyzer(cameraExecutor, LuminosityAnalyzer { luma ->
           Log.d(TAG, "Average luminosity: $luma")
       })
   }
cameraProvider.bindToLifecycle(
   this, cameraSelector, preview, imageCapture, imageAnalyzer)
```

* `startCamera()` 함수에 객체를 만들고, 바인딩 하기 전에 Build를 해준다.
* 그리고 위에서 했던 Capture use Case 와 같이 바인딩해준다.