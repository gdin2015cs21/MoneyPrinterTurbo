# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

# 配置 PostgreSQL 数据库连接
DATABASE_URL = "postgresql://username:password@host:port/dbname"
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 定义数据库模型
class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, index=True)
    document_key = Column(String, index=True)
    target_lang = Column(String)


# 内容类型
class CmContent(Base):
    __tablename__ = "cm_content"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer)
    provider_id = Column(Integer)
    create_type = Column(Integer)
    org_id = Column(Integer)
    uuid = Column(String)
    language = Column(String)
    category_id = Column(Integer)
    category_desc = Column(String)
    content_type = Column(Integer)
    content_format = Column(String)
    purpose = Column(Integer)
    title = Column(String)
    summary = Column(String)
    content = Column(String)
    thumb_imgs = Column(String)
    images = Column(String)
    author = Column(String)
    author_user = Column(String)
    origin = Column(String)
    origin_type = Column(String)
    origin_content_id = Column(Integer)
    origin_url = Column(String)
    origin_trans_state = Column(Integer)
    part_pattern = Column(Integer)
    part_number = Column(Integer)
    pub_type = Column(Integer)
    child_org_manage = Column(Integer)
    download_flag = Column(Integer)
    browser_num = Column(Integer)
    download_num = Column(Integer)
    labels = Column(String)
    labels_path = Column(String)
    score = Column(Float)
    weights = Column(Integer)
    price = Column(Float)
    class_hours = Column(Float)
    credit_type = Column(Integer)
    credit = Column(Float)
    total_duration = Column(Integer)
    total_pages = Column(Integer)
    finish_type = Column(Integer)
    finish_ratio = Column(Float)
    finish_seconds = Column(Integer)
    upload_time = Column(str)
    upload_user = Column(Integer)
    publish_user = Column(str)
    publish_time = Column(str)
    first_publish_time = Column(str)
    bank_type = Column(Integer)
    manage_type = Column(Integer)
    terminal = Column(str)
    audit_user = Column(Integer)
    audit_time = Column(str)
    audit_reason = Column(str)
    state = Column(Integer)
    keywords = Column(str)
    remark = Column(str)


# 内容切块
class CmContentPart(Base):
    __tablename__ = "cm_content_part"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer)
    title = Column(String)
    summary = Column(String)
    content = Column(String)
    thumb_img = Column(String)
    images = Column(String)
    res_type = Column(String)
    res_url = Column(String)
    add_res_url1 = Column(String)
    add_res_url2 = Column(String)
    duration = Column(Integer)
    state = Column(Integer)
    download_flag = Column(Integer)
    upload_time = Column(String)
    upload_user = Column(String)
    upload_user_id = Column(String)
    order_num = Column(Integer)
    remark = Column(String)


# 任务
class DcmTaskMessage(Base):
    __tablename__ = "dcm_task_message"

    id = Column(Integer, primary_key=True, index=True)
    task_type = Column(Integer)
    task_code = Column(String)
    uuid = Column(String)
    message = Column(String)
    state = Column(Integer)
    remark = Column(String)
    create_user = Column(Integer)
    input_config = Column(String)
    output_config = Column(String)
