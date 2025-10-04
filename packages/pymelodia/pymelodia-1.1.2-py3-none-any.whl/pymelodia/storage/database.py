# -*- coding: utf-8 -*-
"""数据库管理模块"""

import sqlite3
import os
import threading
from typing import Optional, Tuple
from ..utils.logger import logger
from pathlib import Path

class MusicDatabase:
    """音乐数据库管理类 - 线程安全版本"""
    
    def __init__(self, db_path: Optional[str] = None):
        """初始化数据库连接"""
        if db_path is None:
            # 确保data目录存在
            DATA_DIR = Path.home() / ".melodia"
            if not os.path.exists(DATA_DIR):
                os.makedirs(DATA_DIR)
            db_path = os.path.join(DATA_DIR, 'data.db')
        
        self.db_path = db_path
        # 使用线程本地存储来避免游标冲突
        self._local = threading.local()
        self._lock = threading.Lock()
        # 初始化主连接来创建表结构
        self._init_connection = sqlite3.connect(db_path, check_same_thread=False)
        self._create_tables()

    def _get_connection(self):
        """获取线程本地的数据库连接"""
        if not hasattr(self._local, 'connection') or self._local.connection is None:
            self._local.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        return self._local.connection
    
    def _get_cursor(self):
        """获取线程本地的数据库游标"""
        connection = self._get_connection()
        if not hasattr(self._local, 'cursor') or self._local.cursor is None:
            self._local.cursor = connection.cursor()
        return self._local.cursor

    def _create_tables(self):
        """创建数据库表"""
        try:
            cursor = self._init_connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS musicBasicData (
                id INTEGER PRIMARY KEY,
                title TEXT,
                subtitle TEXT,
                artist TEXT,
                album TEXT,
                lyric TEXT
            )
            ''')
            self._init_connection.commit()
            cursor.close()
        except Exception as e:
            logger.error(f'创建数据库表失败: {e}')
            raise

    def music_exists(self, music_id: str) -> bool:
        """检查音乐是否存在"""
        try:
            with self._lock:
                cursor = self._get_cursor()
                connection = self._get_connection()
                cursor.execute('SELECT 1 FROM musicBasicData WHERE id = ? LIMIT 1', (music_id,))
                result = cursor.fetchone() is not None
                connection.commit()  # 确保事务完成
                return result
        except Exception as e:
            logger.error(f'检查音乐是否存在时出错: {e}')
            return False

    def detect_repeat_by_nsa(self, name: str, subtitle: str, artist: str) -> bool:
        """通过名称、副标题、艺术家检测重复"""
        try:
            with self._lock:
                cursor = self._get_cursor()
                connection = self._get_connection()
                cursor.execute(
                    'SELECT 1 FROM musicBasicData WHERE subtitle = ? AND title = ? AND artist = ? LIMIT 1', 
                    (subtitle, name, artist)
                )
                result = cursor.fetchone() is not None
                connection.commit()  # 确保事务完成
                return result
        except Exception as e:
            logger.error(f'检测重复音乐时出错: {e}')
            return False

    def add_single_music(self, music_id: str, name: str, subtitle: str, 
                        artist: str, album: str, lyric: str) -> bool:
        """添加单个音乐记录"""
        try:
            with self._lock:
                cursor = self._get_cursor()
                connection = self._get_connection()
                cursor.execute('''
                    INSERT OR IGNORE INTO musicBasicData(id, title, subtitle, artist, album, lyric) 
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (music_id, name, subtitle, artist, album, lyric))
                connection.commit()
                if cursor.rowcount > 0:
                    logger.debug(f'音乐 {name} 已添加到数据库')
                    return True
                else:
                    logger.debug(f'音乐 {name} 已存在于数据库中')
                    return True
        except Exception as e:
            logger.error(f'添加音乐到数据库失败: {e}')
            # 尝试回滚
            try:
                connection = self._get_connection()
                connection.rollback()
            except Exception:
                pass
            return False

    def get_single_music_by_id(self, music_id: str) -> Optional[Tuple]:
        """通过ID获取单个音乐记录"""
        try:
            with self._lock:
                cursor = self._get_cursor()
                connection = self._get_connection()
                cursor.execute('SELECT * FROM musicBasicData WHERE id = ?', (str(music_id),))
                result = cursor.fetchone()
                connection.commit()  # 确保事务完成
                return result
        except Exception as e:
            logger.error(f'获取音乐记录时出错: {e}')
            return None

    def close(self):
        """关闭所有数据库连接"""
        try:
            # 关闭线程本地连接
            if hasattr(self._local, 'cursor') and self._local.cursor:
                self._local.cursor.close()
                self._local.cursor = None
            
            if hasattr(self._local, 'connection') and self._local.connection:
                self._local.connection.close()
                self._local.connection = None
            
            # 关闭主连接
            if self._init_connection:
                self._init_connection.close()
                self._init_connection = None
                
        except Exception as e:
            logger.error(f'关闭数据库连接时出错: {e}')

    def _cleanup_thread_resources(self):
        """清理当前线程的数据库资源"""
        try:
            if hasattr(self._local, 'cursor') and self._local.cursor:
                self._local.cursor.close()
                self._local.cursor = None
            
            if hasattr(self._local, 'connection') and self._local.connection:
                self._local.connection.close()
                self._local.connection = None
                
        except Exception as e:
            logger.error(f'清理线程数据库资源时出错: {e}')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # 如果有异常，尝试回滚当前线程的事务
            try:
                connection = self._get_connection()
                connection.rollback()
            except Exception:
                pass
        self._cleanup_thread_resources()


