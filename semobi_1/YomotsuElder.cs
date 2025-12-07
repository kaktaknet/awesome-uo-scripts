using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Wrinkly Yomotsu corpse" )]
	public class YomotsuElder : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.ParalyzingBlow;
                  return WeaponAbility.ShadowStrike;
            } 

		[Constructable]
		public YomotsuElder() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Yomotsu Elder";
			Body = 255;
			BaseSoundID = 422;

			SetStr( 695, 825 );
			SetDex( 250, 365 );
			SetInt( 15, 40 );

			SetHits( 820, 895 );
			SetMana( 15, 40 );
			SetStam( 250, 365 );

			SetDamage( 50, 76 );

			SetDamageType( ResistanceType.Physical, 100 ); 


			SetResistance( ResistanceType.Physical, 65, 85 );
			SetResistance( ResistanceType.Fire, 30, 50 );
			SetResistance( ResistanceType.Cold, 45, 65 );
			SetResistance( ResistanceType.Poison, 35, 55 );
			SetResistance( ResistanceType.Energy, 25, 50 );

			SetSkill( SkillName.MagicResist, 100.0, 115.0 );
			SetSkill( SkillName.Tactics, 115.0, 130.0 );
			SetSkill( SkillName.Wrestling, 110.0, 130.0 );
			SetSkill( SkillName.Anatomy, 115.0, 130.0 );

			Fame = 15000;
			Karma = -15000;
			
			Tamable = false;

         PackGold( 1500, 1800 ); 
         PackMagicItems( 1, 5 );
			AddItem( new Sandals());
			AddItem( new ExecutionersAxe());
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.FilthyRich );
		}

		public override bool CanRummageCorpses{ get{ return true; } } 
		public override FoodType FavoriteFood{ get{ return FoodType.FruitsAndVegies; } }

                public YomotsuElder( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}