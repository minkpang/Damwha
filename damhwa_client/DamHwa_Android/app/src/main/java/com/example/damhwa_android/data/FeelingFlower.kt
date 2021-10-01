package com.example.damhwa_android.data

import com.google.gson.annotations.SerializedName

data class FeelingFlower(
    @SerializedName("name")
    val name: String,
    @SerializedName("description")
    val description: String,
)