package com.f5.damhwa_android.ui.story

import android.util.Log
import androidx.core.os.bundleOf
import androidx.fragment.app.activityViewModels
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import com.f5.damhwa_android.R
import com.f5.damhwa_android.base.BaseFragment
import com.f5.damhwa_android.data.Flower
import com.f5.damhwa_android.databinding.FragmentStoryRecFlowerBinding
import com.f5.damhwa_android.network.DamhwaInjection
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.disposables.Disposable
import io.reactivex.rxkotlin.addTo

class StoryRecFlowerFragment : BaseFragment<FragmentStoryRecFlowerBinding>(
    R.layout.fragment_story_rec_flower
) {
    private val disposables by lazy { CompositeDisposable() }
    private val storyViewModel by activityViewModels<StoryFragmentViewModel> {
        object : ViewModelProvider.Factory {
            override fun <T : ViewModel?> create(modelClass: Class<T>): T {
                return StoryFragmentViewModel(DamhwaInjection.providerStoryRepository()) as T
            }
        }
    }

    override fun init() {
        super.init()
        binding.backButton.setOnClickListener {
            routeToBack()
        }

        val adapter = RecommendedFlowerAdapter(::routeToFlowerDetail)
        binding.carouselRecycler.adapter = adapter
        binding.carouselRecycler.setIntervalRatio(0.5f)
        binding.carouselRecycler.setAlpha(true)

        storyViewModel.recommendedFlowerListFromStory
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe({ flowers ->
                adapter.flowers = flowers
                adapter.notifyDataSetChanged()
                storyViewModel.clearData()
            }, {
                Log.e("ErrorLogger - StoryRecFlower - recommFlowerList", it.message.toString())
            })
            .addToDisposable()
    }


    private fun routeToBack() =
        findNavController().navigate(R.id.action_storyRecFlowerFragment_to_storyFragment)

    private fun routeToFlowerDetail(flower: Flower) =
        findNavController().navigate(
            R.id.action_storyRecFlowerFragment_to_storyFlowerDetailFragment,
            bundleOf("flower" to flower)
        )

    private fun Disposable.addToDisposable(): Disposable = addTo(disposables)

    override fun onDestroy() {
        disposables.clear()
        super.onDestroy()
    }
}