from typing import Optional
from fastapi import APIRouter, Depends, File, UploadFile, BackgroundTasks
from pydantic.types import UUID4

from app.api.api_v1.uploads.uploads_utils import handle_upload_files
from app.api.api_v1.uploads.uploads_utils import verify_uploaded_file_type
from app.core.auth import get_current_active_user, get_current_active_superuser
from app.api.api_v1.bg_task import process_images_background
from app.ocr_sys_v2.ocr_read import read_text
# from app.document_ai.process import process_ddi_document

uploads_router = u = APIRouter()

@u.post(
    "/upload",
    dependencies = [Depends(verify_uploaded_file_type)],
    responses = {400: {"description": "Returned when the uploaded file does not match the valid params"}}
)
def upload_form(
    bg_tasks: BackgroundTasks,
    upload_id: Optional[UUID4],
    form_type: int,
    files: list[UploadFile],
    current_user = Depends(get_current_active_superuser),
):
    paths = handle_upload_files(files)
    for path in paths:
        s = read_text(str(path))
    return s