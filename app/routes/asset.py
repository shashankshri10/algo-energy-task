from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app.models.asset import Asset
from app.models.start_end import StartEnd
from app.services.asset_service import AssetService
from ..dependencies import verify_token

router = APIRouter(
    prefix="/asset",
    tags=["asset"],
    responses={404: {"description": "Not found"}},
)
asset_service = AssetService()

@router.post("/create/")
async def create_asset(asset:Asset,user_id:Annotated[str,Depends(verify_token)]):
    try:
        res_dict = await asset_service.create_asset(asset,user_id)
        if res_dict["status"]:
            return {"message": res_dict["message"]}
        else:
            raise HTTPException(status_code=401, detail=res_dict["message"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/byuser/{user_id}")
async def get_assets_by_user_id(user_id: str, current_user_id: Annotated[str,Depends(verify_token)]):
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    assets = await asset_service.get_assets_by_user_id(user_id)
    if not assets:
         raise HTTPException(status_code=404, detail="Assets not found")
    return assets

@router.get("/byname/{name}")
async def get_assets_by_name(name: str,user_id:Annotated[str,Depends(verify_token)]):
    assets = await asset_service.get_assets_by_name(name)
    if not assets:
         raise HTTPException(status_code=404, detail="Assets not found")
    return assets

@router.get("/bytype/{type}")
async def get_assets_by_type(type: str,user_id:Annotated[str,Depends(verify_token)]):
    assets = await asset_service.get_assets_by_type(type)
    if not assets:
         raise HTTPException(status_code=404, detail="Assets not found")
    return assets

@router.get("/byoperational-status/{operational_status}")
async def get_assets_by_operational_status(operational_status: str,user_id:Annotated[str,Depends(verify_token)]):
    assets = await asset_service.get_assets_by_operational_status(operational_status)
    if  len(assets)==0:
         raise HTTPException(status_code=404, detail="Assets not found")
    return assets

@router.get("/bylocation/{location}")
async def get_assets_by_location(location: str,user_id:Annotated[str,Depends(verify_token)]):
    assets = await asset_service.get_assets_by_location(location)
    if  len(assets)==0:
         raise HTTPException(status_code=404, detail="Assets not found")
    return assets

@router.post("/bydate/")
async def get_assets_by_purchase_date(start_end:StartEnd,user_id:Annotated[str,Depends(verify_token)]):
    assets = await asset_service.get_assets_by_purchase_date(start_end,user_id)
    if len(assets)==0:
        raise HTTPException(status_code=404, detail="Assets not found")
    return assets