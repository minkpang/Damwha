package com.ssafy.damhwa.db.repository;

import com.ssafy.damhwa.db.entity.History;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface HistoryRepository extends JpaRepository<History, Long> {

    List<History> findAllByUserno(long userno);
}