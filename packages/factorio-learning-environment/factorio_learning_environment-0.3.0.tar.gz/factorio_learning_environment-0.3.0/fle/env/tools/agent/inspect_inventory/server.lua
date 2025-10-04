global.actions.inspect_inventory = function(player_index, is_character_inventory, x, y, entity, all_players)
    local position = {x=x, y=y}
    local player = global.agent_characters[player_index]
    local surface = player.surface
    local is_fast = global.fast
    local automatic_close = True

    local function get_player_inventory_items(player)

       local inventory = player.get_main_inventory()
       if not inventory or not inventory.valid then
           return nil
       end

       local item_counts = inventory.get_contents()
       return item_counts
    end

    local function get_inventory()
       local closest_distance = math.huge
       local closest_entity = nil

       local area = {{position.x - 2, position.y - 2}, {position.x + 2, position.y + 2}}
       local buildings = surface.find_entities_filtered({ area = area, force = "player", name = entity })
       -- game.print("Found "..#buildings.. " "..entity)
       for _, building in ipairs(buildings) do
           if building.name ~= 'character' then
               local distance = ((position.x - building.position.x) ^ 2 + (position.y - building.position.y) ^ 2) ^ 0.5
               if distance < closest_distance then
                   closest_distance = distance
                   closest_entity = building
               end
           end
       end
       
       if closest_entity == nil then
           error("No entity at given coordinates.")
       end
       if not closest_entity or not closest_entity.valid then
           error("No valid entity at given coordinates.")
       end

       if not is_fast then
           player.opened = closest_entity
           script.on_nth_tick(60, function()
               if automatic_close == True then
                   if closest_entity and closest_entity.valid then
                       player.opened = nil
                   end
                   automatic_close = False
               end
           end)
       end

       if closest_entity.type == "furnace" then
           if not closest_entity or not closest_entity.valid then
               error("No valid entity at given coordinates.")
           end
           local source = closest_entity.get_inventory(defines.inventory.furnace_source).get_contents()
           local output = closest_entity.get_inventory(defines.inventory.furnace_result).get_contents()
           for k, v in pairs(output) do
               source[k] = (source[k] or 0) + v
           end
           return source
       end
       if closest_entity.type == "assembling-machine" then
           if not closest_entity or not closest_entity.valid then
               error("No valid entity at given coordinates.")
           end
           local source = closest_entity.get_inventory(defines.inventory.assembling_machine_input).get_contents()
           local output = closest_entity.get_inventory(defines.inventory.assembling_machine_output).get_contents()
           for k, v in pairs(output) do
               source[k] = (source[k] or 0) + v
           end
           return source
       end
       if closest_entity.type == "lab" then
           if not closest_entity or not closest_entity.valid then
               error("No valid entity at given coordinates.")
           end
           return closest_entity.get_inventory(defines.inventory.lab_input).get_contents()
       end
       -- Handle centrifuge inventories
       if closest_entity.type == "assembling-machine" and closest_entity.name == "centrifuge" then
           if not closest_entity or not closest_entity.valid then
               error("No valid entity at given coordinates.")
           end
           local source = closest_entity.get_inventory(defines.inventory.assembling_machine_input).get_contents()
           local output = closest_entity.get_inventory(defines.inventory.assembling_machine_output).get_contents()
           -- Merge input and output contents
           for k, v in pairs(output) do
               source[k] = (source[k] or 0) + v
           end
           return source
       end
       if not closest_entity or not closest_entity.valid then
           error("No valid entity at given coordinates.")
       end
       return closest_entity.get_inventory(defines.inventory.chest).get_contents()
    end

    local player = global.agent_characters[player_index]
    if not player then
       error("Player not found")
    end

    if all_players then
        local all_inventories = {}
        for _, p in pairs(global.agent_characters) do
            local inventory_items = get_player_inventory_items(p)
            if inventory_items then
                table.insert(all_inventories, inventory_items)
            else
                table.insert(all_inventories, {})
            end
        end
        return dump(all_inventories)
    end

    if is_character_inventory then
       local inventory_items = get_player_inventory_items(player)
       if inventory_items then
           return dump(inventory_items)
       else
           error("Could not get player inventory")
       end
    else
       local inventory_items = get_inventory()
       if inventory_items then
           return dump(inventory_items)
       else
           error("Could not get inventory of entity at "..x..", "..y)
       end
    end
end