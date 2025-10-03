from aiod.calls import calls

(
    get_list,
    counts,
    get_asset,
    register,
    replace,
    update,
    delete,
    get_asset_from_platform,
    get_content,
    get_assets_async,
    get_list_async,
) = calls.wrap_common_calls(asset_type="platforms", module=__name__)
